from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.config import  config
import uvicorn

# heldth route

from app.api.heldth import router as heldth

app=FastAPI()




origins = [
   "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# register
app.include_router(heldth)


if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=config.port, reload=config.debug)