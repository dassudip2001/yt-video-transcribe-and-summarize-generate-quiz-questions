from typing import Optional

from pydantic import BaseModel


class GenerateRequest(BaseModel):
    "generate request"
    url: str


class QuizMCQItem(BaseModel):
    question: str
    options: list[str]
    answer: str


class QuizTrueFalseItem(BaseModel):
    question: str
    answer: bool


class QuizShortAnswerItem(BaseModel):
    question: str
    answer: str


class QuizModel(BaseModel):
    mcq: list[QuizMCQItem]
    true_false: list[QuizTrueFalseItem]
    short_answer: list[QuizShortAnswerItem]


class GenerateResponse(BaseModel):
    summary: str
    quiz: Optional[QuizModel] = None
    quiz_raw: Optional[str] = None
    parse_error: Optional[str] = None