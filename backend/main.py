import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

audio_file=open(r"C:\Users\sudip\Downloads\langgrapth\backend\d3534a68-ce84-44e4-9f72-065923d99a27.webm","rb")

transcript=client.audio.transcriptions.create(model="whisper-1", file=audio_file)


print(transcript.text)