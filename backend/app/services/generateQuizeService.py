import asyncio
import json
import re
from typing import Optional

from app.config.openai import openAiClient
from app.schema.schemas import QuizModel

async def generateQuize(text: str):
    # NOTE: This prompt contains JSON braces `{ ... }`. Do NOT use an f-string here,
    # otherwise Python will try to interpret those braces as format placeholders.
    QUIZE_GENERATION_PROMPT = """
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
        {SUMMARY_OUTPUT}
        """
    raw_text: Optional[str] = None
    try:
        # openAiClient.responses.create() is blocking (sync SDK), so run it in a thread.
        response = await asyncio.to_thread(
            openAiClient.responses.create,
            model="gpt-4o",
            input=QUIZE_GENERATION_PROMPT.replace("{SUMMARY_OUTPUT}", text),
        )

        raw_text = response.output[0].content[0].text

        # The model is instructed to return JSON, but sometimes it includes extra text.
        # Try parsing the full string first; if it fails, extract the outermost `{ ... }`.
        try:
            parsed = json.loads(raw_text)
        except json.JSONDecodeError:
            match = re.search(r"\{.*\}", raw_text, flags=re.DOTALL)
            if not match:
                raise
            parsed = json.loads(match.group(0))

        quiz = QuizModel.model_validate(parsed)
        return {"quiz": quiz.model_dump(), "quiz_raw": raw_text, "parse_error": None}
    except Exception as e:
        # Return raw error info so the API can include it in `GenerateResponse`.
        return {"quiz": None, "quiz_raw": raw_text, "parse_error": str(e)}