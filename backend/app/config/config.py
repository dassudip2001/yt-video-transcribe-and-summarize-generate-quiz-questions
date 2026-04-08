import os
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()

class Config(BaseModel):
    debug:bool=False
    port:int=8000
    OPENAI_API_KEY:str=os.getenv("OPENAI_API_KEY")
config=Config()