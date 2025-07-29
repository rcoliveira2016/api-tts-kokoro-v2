from fastapi.responses import StreamingResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .audio_handler import audio_stream
app = FastAPI()

origins = [
    "*",
] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Message": "Ok"}

@app.get("/healthcheck")
def read_healthcheck():
    return {"Message": "Ok"}

@app.get("/tts")
async def tts(text: str, voice: str = "pf_dora"):
    """Gera áudio TTS via Kokoro e envia como stream."""   
    return StreamingResponse(audio_stream(text, voice), media_type="audio/wav")