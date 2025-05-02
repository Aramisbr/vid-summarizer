from moviepy import VideoFileClip
from django.conf import settings
from pathlib import Path
import os
from faster_whisper import WhisperModel
from openai import OpenAI

model = WhisperModel("tiny", device="cpu", compute_type="int8")

class Transcricao:
    def __init__(self, path_video):
        self.path_video = path_video
        self.audio_path = settings.BASE_DIR / "audio_file" / (Path(path_video).stem + ".wav")
    
    # Extrai o áudio do vídeo
    def save_tempfile (self):
        video = VideoFileClip(self.path_video)
        try:
            video.audio.write_audiofile(
                str(self.audio_path),  
                fps=16000,             
                nbytes=2,              
                bitrate="64k",         
                codec='pcm_s16le'      
            )
        finally:
            video.close() # Garantir que o vídeo feche, mesmo se der erro

    # Transcreve e junta todos os trechos do áudio
    def transcrever (self):
        self.save_tempfile()
        try:
            segments, _ = model.transcribe(str(self.audio_path), language="pt")
            texto = " ".join(segment.text for segment in segments)
        finally:
            if os.path.exists(self.audio_path):
                os.remove(self.audio_path)      # Remove o áudio após o uso

        return texto

# Gerar resumo com GPT 3.5 Turbo
def gerar_resumo(texto):
    client = OpenAI(api_key=settings.SK_OPENAI)
    messages=[
        {"role": "system", "content": "Você é um assistente especialista em resumos de vídeos em português."},
        {"role": "user", "content": f"Resuma esse texto de forma clara, adaptando o tamanho do resumo de acordo com a duração do vídeo:\n\n {texto}"}]
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages = messages
    )

    return response.choices[0].message.content

