from pydantic import BaseModel, Field
from datetime import datetime


class QuestionResponseBase(BaseModel):
    user_id: str | None
    content_id: str | None
    response: str | None
    category: str | None
    fruit: str | None
    prompt: str | None


class QuestionResponse(QuestionResponseBase):
    answer_correct: bool = Field(default=True)
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())
