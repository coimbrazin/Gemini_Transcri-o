from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

video_url = 'https://youtu.be/Ys7-6_t7OEQ?feature=shared'

def get_video_title(video_url):
  """Extrai o título de um vídeo do Youtube."""
  try:
    yt = YouTube(video_url)
    return yt.title
  except Exception as e:
    print(f"Erro ao obter o título do vídeo: {e}")
    return None
  
def get_transcript(video_id):
  """Obtém a transcrição de um vídeo do Youtube."""
  try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ' '.join([entry['text'] for entry in transcript])
    return text
  except Exception as e:
    print(f"Erro ao obter a transcrição: {e}")
    return None

def extract_video_id(url):
  """Extrai o ID do vídeo da URL do Youtube."""
  try:
    yt = YouTube(url)
    return yt.video_id
  except Exception as e:
    print(f"Erro ao entrair o ID do vídeo: {e}")
    return None
# Uso das funções
title = get_video_title(video_url)
print(f"Título do vídeo: {title}")

video_id = extract_video_id(video_url)
print(f"ID do vídeo: {video_id}")

transcript = get_transcript(video_id)
print(f"Transcrição do vídeo: {transcript}")