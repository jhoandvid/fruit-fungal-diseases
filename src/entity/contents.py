from pydantic import BaseModel, Field, validator
from typing import Optional, List
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
    question: str
    fruit: str


class UpdateContents(BaseModel):
    title: Optional[str]
    category: Optional[str]
    fruit: Optional[str]
    information: Optional[List]

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

    @validator("information", pre=True, always=True)
    def validate_information(cls, value):
        if value is None:
            return []
        return value