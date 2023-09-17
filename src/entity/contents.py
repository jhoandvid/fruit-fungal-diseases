from pydantic import BaseModel, Field
from datetime import datetime
import json


class ContentsEntityBase(BaseModel):
    category: str
    fruit: str


class ContentsEntity(ContentsEntityBase):
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())

    class Config:
        schema_extra = {
            "example": {
                "category": "hongos",
                "fruit": "kiwi"
            }
        }

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class ConsultContentInformation(BaseModel):
    content_id: str
    question: str
    category: str
    fruit: str


class UpdateContents(BaseModel):
    title: str | None
    category: str | None
    fruit: str | None
    information: list | None

    class Config:
        schema_extra = {
            "example": {
                "title": "enfermedades de la plata",
                "category": "hongos",
                "fruit": "kiwi"
            }
        }

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
