# api-tts-kokoro-v2

Este projeto é uma API de Text-to-Speech (TTS) construída com [FastAPI](https://fastapi.tiangolo.com/) e [kokoro](https://pypi.org/project/kokoro/). O objetivo é fornecer uma interface simples para conversão de texto em áudio.

## Funcionalidades

- Endpoint para conversão de texto em áudio (TTS)
- Streaming de áudio gerado
- Configuração pronta para CORS
- Gerenciamento moderno de dependências com [uv](https://github.com/astral-sh/uv)

## Requisitos

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) instalado

## Instalação

1. Instale o `uv` (gerenciador de dependências ultrarrápido):

   ```sh
   pip install uv
   ```

2. Instale as dependências do projeto:

   ```sh
   uv sync
   ```

   Ou, para instalar e criar ambiente isolado:

   ```sh
   uv venv
   uv pip install -r pyproject.toml
   ```

## Como executar

1. Ative o ambiente virtual (se criado):

   ```sh
   source .venv/bin/activate
   ```

2. Execute a API com uv:

   ```sh
   uv run uvicorn app.main:app --reload
   ```

   Ou simplesmente use o comando:

   ```sh
   uv run fastapi dev
   ```

O servidor de desenvolvimento iniciará em `http://localhost:8000` com hot-reload ativado.

## Endpoints

- `GET /` — Verifica se a API está funcionando.
- `GET /tts` — (Em desenvolvimento) Gera áudio a partir de texto.
- `GET /stream-audio` — Faz streaming do arquivo `output.wav` como áudio.

## Sobre o uv

O [uv](https://github.com/astral-sh/uv) é uma ferramenta moderna para gerenciamento de ambientes e dependências Python, oferecendo instalação ultrarrápida e compatibilidade com arquivos `pyproject.toml`. Ele substitui o uso tradicional do `pip` e do `venv`, tornando o fluxo de trabalho mais simples e eficiente.

## Usando Docker

Este projeto também pode ser executado usando Docker. Siga os passos abaixo para construir e executar o container:

### Construir a imagem Docker

1. Certifique-se de que o Docker está instalado e em execução no seu sistema.
2. No diretório raiz do projeto, construa a imagem Docker:

   ```sh
   docker build -t api-tts-kokoro-v2 .
   ```

### Executar o container

1. Após construir a imagem, execute o container:

   ```sh
   docker run -p 8085:80 api-tts-kokoro-v2
   ```

2. A API estará disponível em `http://localhost:8085`.

## Licença

MIT