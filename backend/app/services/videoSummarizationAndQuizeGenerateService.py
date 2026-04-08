
from app.services import ytService,whisperService,generateQuizeService,generateSummarizationService

async def videoSummarizationAndQuizeGenerate(req:str):
    videoPath=await ytService(req)
    print("Video Path",videoPath)
    print("..........................................................................")
    textResponse= await whisperService(videoPath)
    print("Text", textResponse)
    print("..........................................................................")
    generateSummary=await generateSummarizationService(textResponse)
    print(generateSummary)
    print("...........................................................................")


    return {generateSummary}
    


