from django.shortcuts import render
from .models import Video
from django.http import HttpResponse
from .utils import Transcricao, gerar_resumo
from openai import OpenAI
import os



def home (request):
    if request.method == 'GET':
        return render (request, 'home.html')
    elif request.method == 'POST':
        # Pega o vídeo e o título enviados.
        titulo = request.POST.get ('titulo')
        video = request.FILES.get ('video')

        # Salva o vídeo temporariamente
        video_upload = Video(titulo=titulo, video=video)
        video_upload.save()
        
        # Inicia a transcrição 
        transcricao = Transcricao(video_upload.video.path)
        transcript = transcricao.transcrever()

        # Salva a transcrição e resumo no banco
        video_upload.transcricao = transcript
        video_upload.resumo = gerar_resumo(transcript)
        video_upload.save()

        # Após processamento, remove o vídeo
        if os.path.exists(video_upload.video.path):
            os.remove(video_upload.video.path)

        # Mostrar a página de resultado
        return render(request, 'resultado.html', {'video': video_upload})

