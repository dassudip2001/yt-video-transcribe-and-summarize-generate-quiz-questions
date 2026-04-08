
import asyncio

from app.services import ytService,whisperService,generateQuizeService,generateSummarizationService

async def videoSummarizationAndQuizeGenerate(req:str):
    # yt-dlp download is blocking, so run it in a thread.
    videoPath = await asyncio.to_thread(ytService.download_video, req)
    print("Video Path",videoPath)
    print("..........................................................................")
    # Whisper transcription is blocking (OpenAI SDK sync), so run it in a thread.
    textResponse = await asyncio.to_thread(whisperService.transcribe_audio, videoPath)
    print("Text", textResponse)
    print("..........................................................................")
    generateSummary = await generateSummarizationService.generateSummarization(textResponse)
    print(generateSummary)
    print("...........................................................................")

    generateQuize = await generateQuizeService.generateQuize(generateSummary)


    # `generateQuize` returns: { quiz, quiz_raw, parse_error }
    return {"summary": generateSummary, **generateQuize}
    


