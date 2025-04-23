from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound

video_url = 'https://youtu.be/Ys7-6_t7OEQ?feature=shared'

def get_video_title(video_url):
    """Extrai o título de um vídeo do Youtube."""
    try:
        yt = YouTube(video_url)
        return yt.title
    except Exception as e:
        print(f"Erro ao obter o título do vídeo: {e}")
        return None

def get_transcript(video_id, language='en'):
    """Obtém a transcrição de um vídeo do Youtube para o idioma especificado."""
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
    """Extrai o ID do vídeo da URL do Youtube."""
    try:
        yt = YouTube(url)
        return yt.video_id
    except Exception as e:
        print(f"Erro ao entrair o ID do vídeo: {e}")
        return None
