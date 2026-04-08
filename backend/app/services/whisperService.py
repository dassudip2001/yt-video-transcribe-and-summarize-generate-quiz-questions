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
from app.config.openai import openAiClient


def transcribe_audio(file_path):
    audio_file=open(file_path)
    transcript=openAiClient.audio.transcriptions.create(model="whisper-1", file=audio_file)
    print(transcript.text)
    return transcript.text