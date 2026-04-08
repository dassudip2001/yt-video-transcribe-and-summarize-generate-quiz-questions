from pydantic import BaseModel



class GenerateRequest(BaseModel):
    "generate request"
    url:str