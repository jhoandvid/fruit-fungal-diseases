from fastapi import APIRouter
from src.entity.fruit_fungal_diseases import FruitFungalDisease
from src.service.fruit_fungal_diseases_service import FruitFungalDiseasesService
from fastapi import Request

fruit_fungal_diseases_router = APIRouter()

fruit_fungal_diseases_service = FruitFungalDiseasesService()


@fruit_fungal_diseases_router.post("/diseases")
async def create_fruit_diseases(request: Request, fruit_diseases: FruitFungalDisease):
    user_id = request.state.user_id
    return fruit_fungal_diseases_service.create_fruit_fungal_disease(user_id, fruit_diseases)


@fruit_fungal_diseases_router.get("/diseases")
async def get_fruit_diseases():
    return fruit_fungal_diseases_service.find_fruit_funga_disease()


@fruit_fungal_diseases_router.get("/search")
async def name(query: str = ''):
    return fruit_fungal_diseases_service.find_disease_by_name(query)

@fruit_fungal_diseases_router.get("/diseases/{id}")
async def get_disease_by_id(id: str):
    return fruit_fungal_diseases_service.find_fruit_deseases_by_id(id)