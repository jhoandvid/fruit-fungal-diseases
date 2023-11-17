from fastapi import APIRouter, Request
from src.service.rating_aplication_service import RatingAplicationService
from src.entity.raiting_aplication import RatingAplication
rating_aplication_router = APIRouter()
rating_aplication_service = RatingAplicationService()


@rating_aplication_router.post("/rating")
async def create_rating_aplication(request: Request, rating_aplication: RatingAplication):
    rating_aplication.user_id = request.state.user_id
    return rating_aplication_service.create_rating_aplication(rating_aplication)
@rating_aplication_router.get("/rating")
async def get_rating_aplication(request: Request):
    user_id = request.state.user_id
    return rating_aplication_service.find_rating_aplication(user_id)

