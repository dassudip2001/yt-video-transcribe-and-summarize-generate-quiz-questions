import yt_dlp
import uuid
from pathlib import Path

def download_video(url: str):
    "Download video form url "
    unique_id=str(uuid.uuid4())
    # Always save into `backend/` root so other services can find the file.
    backend_root = Path(__file__).resolve().parents[2]
    ydl_opts={
       'format': 'bestaudio/best',
        'outtmpl': str(backend_root / f'{unique_id}.%(ext)s'),
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info=ydl.extract_info(url,download=True)
        actual_ext = info.get('ext') or 'webm'
        return str(backend_root / f'{unique_id}.{actual_ext}')


    