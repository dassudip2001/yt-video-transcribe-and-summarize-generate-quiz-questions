# from faster_whisper import WhisperModel

# W_client=WhisperModel("base")


# def transcribe_audio(file_path:str):
#     segments,_=W_client.transcribe(file_path)
#     text=" ".join([seg.text for seg in segments])
#     print(text)
#     return text

# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# client=OpenAI()

# audio_file=open(r"C:\Users\sudip\Downloads\langgrapth\backend\d3534a68-ce84-44e4-9f72-065923d99a27.webm","rb")

# transcript=client.audio.transcriptions.create(model="whisper-1", file=audio_file)


# print(transcript.text)
from pathlib import Path

from app.config.openai import openAiClient


def _resolve_audio_path(file_path: str) -> Path:
    """
    Resolve `file_path` to an actual file path.

    If you pass an absolute path, it's used as-is.
    If you pass a relative path/filename, it's treated as relative to `backend/` folder.
    """
    candidate = Path(file_path)
    if candidate.is_absolute():
        return candidate

    # `whisperService.py` is in `backend/app/services/`, so parents[2] is `backend/`.
    backend_root = Path(__file__).resolve().parents[2]
    return backend_root / candidate


def transcribe_audio(file_path: str) -> str:
    audio_path = _resolve_audio_path(file_path)
    if not audio_path.exists():
        raise FileNotFoundError(
            f"Audio file not found: {audio_path}\n"
            "Tip: if you placed the file in the `backend/` root, call "
            "transcribe_audio('your_file.webm')."
        )

    # Openai needs a file handle; keep it closed after the request.
    with audio_path.open("rb") as audio_file:
        transcript = openAiClient.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
        )

    return transcript.text