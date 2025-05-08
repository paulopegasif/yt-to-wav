from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/download")
async def download_audio(req: Request):
    data = await req.json()
    url = data.get("url")

    # Validação inicial: checa se o link é do YouTube
    if not url or not ("youtube.com" in url or "youtu.be" in url):
        raise HTTPException(status_code=400, detail="URL inválida: deve ser um link do YouTube")

    # Verificar se a URL é válida e obter o título com timeout
    try:
        title = subprocess.check_output(
            ["yt-dlp", "--get-title", url],
            text=True,
            timeout=10
        ).strip()
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Tempo excedido ao validar o vídeo")
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=400, detail="URL inválida ou vídeo não encontrado")

    # Limpa o título para criar o nome do arquivo
    safe_title = "".join(c for c in title if c.isalnum() or c in " _-").rstrip()
    output_path = f"/tmp/{safe_title}.wav"

    # Baixar e converter o áudio
    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "wav",
        "-o", output_path,
        url
    ]

    try:
        subprocess.run(command, check=True, timeout=120)
        if not os.path.exists(output_path):
            raise HTTPException(status_code=500, detail="Falha ao gerar o arquivo de áudio")
        with open(output_path, "rb") as file:
            content = file.read()
            headers = {
                "Content-Disposition": f'attachment; filename="{safe_title}.wav"'
            }
            return Response(content, media_type="audio/wav", headers=headers)
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Tempo excedido ao baixar o vídeo")
    except subprocess.CalledProcessError as e:
        print("Erro no subprocess: ", e)
        raise HTTPException(status_code=500, detail="Erro ao processar o vídeo")
    finally:
        # Limpeza do arquivo temporário
        if os.path.exists(output_path):
            os.remove(output_path)
    
@app.get("/")
def root():
    return {"message": "YT-to-WAV backend is live"}

@app.get("/health")
def health():
    return {"status": "ok"}