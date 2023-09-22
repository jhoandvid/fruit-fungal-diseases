from fastapi import APIRouter
from src.entity.fruit_fungal_diseases import FruitFungalDisease
from src.service.fruit_fungal_diseases_service import FruitFungalDiseasesService

fruit_fungal_diseases_router = APIRouter()

fruit_fungal_diseases_service = FruitFungalDiseasesService()


@fruit_fungal_diseases_router.post("/diseases")
async def create_fruit_diseases(fruit_diseases: FruitFungalDisease):
    user_id = ""
    return fruit_fungal_diseases_service.create_fruit_fungal_disease(user_id, fruit_diseases)


@fruit_fungal_diseases_router.get("/diseases")
async def get_fruit_diseases():
    return fruit_fungal_diseases_service.find_fruit_funga_disease()
