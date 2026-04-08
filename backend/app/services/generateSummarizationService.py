from app.config.openai import openAiClient


async def generateSummarization(text:str):
    SUMMARIZATION_PROMPT=f"""
        You are a professional summarizer.

        Summarize the following text:

        Rules:
        - Keep it between 150–200 words
        - Focus on key ideas, concepts, and insights
        - Avoid unnecessary details
        - Make it easy to understand

        TEXT:
        {{text}}
    """

    try:
        response=await openAiClient.responses.create(
            model="gpt-4o",
            input=SUMMARIZATION_PROMPT.replace(f"{{text}}",text)
        );
        return  response.output[0].content[0].text
    except Exception as e:
        return str(e)