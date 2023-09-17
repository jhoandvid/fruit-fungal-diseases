from fastapi import APIRouter
from src.entity.fruit_fungal_diseases import FruitFungalDisease

fruit_fungal_diseases_router = APIRouter()


@fruit_fungal_diseases_router.post("/diseases")
async def get_diseases(fruit_diseases: FruitFungalDisease):
    return {"diseases": ["Apple", "Banana", "Cherry"]}
