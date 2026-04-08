from nt import replace
from app.config.openai import openAiClient

async def generateQuize(text:str):
    QUIZE_GENERATION_PROMPT=f""" 
        You are an expert teacher.

        Create a quiz based on the following summary.

        Rules:
        - 5 MCQs (4 options each, one correct)
        - 2 True/False
        - 2 Short Answer
        - Questions should test understanding and reasoning

        Output in JSON format:

        {
        "mcq": [
            {
            "question": "...",
            "options": ["A", "B", "C", "D"],
            "answer": "..."
            }
        ],
        "true_false": [
            {
            "question": "...",
            "answer": true
            }
        ],
        "short_answer": [
            {
            "question": "...",
            "answer": "..."
            }
        ]
        }

        SUMMARY:
        {{SUMMARY_OUTPUT}}
        """
    try:    
        response=await openAiClient.responses.create(
            model="gpt-4o",
            input=QUIZE_GENERATION_PROMPT.replace(f"{{SUMMARY_OUTPUT}}",text)
        );
        return response.output[0].content[0].text
    except Exception as e:
        return str(e)    