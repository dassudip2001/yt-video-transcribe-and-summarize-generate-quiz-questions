from fastapi import APIRouter
from app.services import videoSummarizationAndQuizeGenerateService
from app.schema.schemas import GenerateRequest
router=APIRouter()


@router.post("/generate")
async def generate_summarize_quize(req:GenerateRequest):
    data=req.model_dump()
    url=data['url']

    response= await videoSummarizationAndQuizeGenerateService(url)
    return {"response":response}