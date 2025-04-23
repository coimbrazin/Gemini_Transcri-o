from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound

def get_video_title(video_url):
    try:
        yt = YouTube(video_url)
        return yt.title
    except Exception as e:
        print(f"Erro ao obter o título do vídeo: {e}")
        return None

def get_transcript(video_id, language='pt'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        text = ' '.join([entry['text'] for entry in transcript])
        return text
    except NoTranscriptFound:
        print(f"Não foi encontrada transcrição para o idioma: {language}")
        return None
    except Exception as e:
        print(f"Erro ao obter a transcrição: {e}")
        return None

def extract_video_id(url):
    try:
        yt = YouTube(url)
        return yt.video_id
    except Exception as e:
        print(f"Erro ao entrar o ID do vídeo: {e}")
        return None
