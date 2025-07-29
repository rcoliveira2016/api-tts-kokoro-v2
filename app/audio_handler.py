import io
import struct
import soundfile as sf
from kokoro import KPipeline

pipeline = KPipeline(lang_code='p', repo_id='hexgrad/Kokoro-82M')

def create_wav_header(sample_rate=24000, bits_per_sample=16, channels=1):
    """Creates WAV header with specified parameters."""
    header = bytearray()
    
    # RIFF chunk descriptor (12 bytes)
    header.extend(b'RIFF')
    header.extend(struct.pack('<I', 0))  # Placeholder for file size
    header.extend(b'WAVE')
    
    # fmt sub-chunk (24 bytes)
    header.extend(b'fmt ')
    header.extend(struct.pack('<I', 16))  # Subchunk1Size (16 for PCM)
    header.extend(struct.pack('<H', 1))   # AudioFormat (1 for PCM)
    header.extend(struct.pack('<H', channels))  # NumChannels
    header.extend(struct.pack('<I', sample_rate))  # SampleRate
    byte_rate = sample_rate * channels * bits_per_sample // 8
    header.extend(struct.pack('<I', byte_rate))  # ByteRate
    block_align = channels * bits_per_sample // 8
    header.extend(struct.pack('<H', block_align))  # BlockAlign
    header.extend(struct.pack('<H', bits_per_sample))  # BitsPerSample
    
    # data sub-chunk (8 bytes)
    header.extend(b'data')
    header.extend(struct.pack('<I', 0))  # Placeholder for data size
    
    return bytes(header)

async def audio_stream(text: str, voice: str = "pf_dora"):
    """Gera áudio TTS via Kokoro e envia como stream."""
    yield create_wav_header()

    buffer = io.BytesIO()
    with sf.SoundFile(buffer, mode='w', samplerate=24000, channels=1, format='WAV') as f:
        for gs, ps, audio in pipeline(text, voice=voice, speed=.8):
            f.write(audio)
            buffer.seek(0)
            data = buffer.read()
            yield data
            buffer.seek(0)
            buffer.truncate(0)