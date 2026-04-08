from openai import OpenAI
from app.config.config import config



openAiClient = OpenAI(api_key=config.OPENAI_API_KEY)

