from pydantic import BaseModel, Field


class RatingAplicationBase(BaseModel):
    rating: float
    comment: str = Field(default="")


class RatingAplication(RatingAplicationBase):
    user_id: str = Field(default="")

    class Config:
        schema_extra = {
            "example": {
                "rating": "2.0",
                "comment": "Comentario de la aplicacion"
            }
        }