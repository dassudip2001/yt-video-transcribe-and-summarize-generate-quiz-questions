from fastapi import APIRouter
from app.services import videoSummarizationAndQuizeGenerateService
from app.schema.schemas import GenerateRequest, GenerateResponse
router=APIRouter()


@router.post("/generate", response_model=GenerateResponse)
async def generate_summarize_quize(req:GenerateRequest):
    data=req.model_dump()
    url=data['url']

    response= await videoSummarizationAndQuizeGenerateService.videoSummarizationAndQuizeGenerate(url)
    return response