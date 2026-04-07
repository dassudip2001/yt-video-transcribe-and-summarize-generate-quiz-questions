import yt_dlp
import uuid

def download_video(url: str):
    unique_id=str(uuid.uuid4())
    ydl_opts={
       'format': 'bestaudio/best',
        'outtmpl': f'{unique_id}.%(ext)s',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info=ydl.extract_info(url,download=True)
        actual_ext = info.get('ext')
        return f"{unique_id}.{actual_ext}"


    