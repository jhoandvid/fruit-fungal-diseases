from src.entity.fruit_fungal_diseases import FruitFungalDisease
from src.database.repository.fruit_fungal_diseases_repository import FruitFungalDiaseasesRepository
from fastapi import HTTPException, status

fruit_fungal_disease_repository = FruitFungalDiaseasesRepository()


class FruitFungalDiseasesService:
    def create_fruit_fungal_disease(self, id_user: str, fruit_funga_disease: FruitFungalDisease):
        fruit_funga_disease.user_id = id_user
        fruit_disease = fruit_fungal_disease_repository.create_fruit_fungal_diasease(fruit_funga_disease.dict())
        return fruit_disease

    def find_fruit_funga_disease(self):
        response_fruits = fruit_fungal_disease_repository.find_fruit_fungal_disease()
        if response_fruits is None:
            return []
        serialized_response_fruit = []
        for response_fruit in response_fruits:
            response_fruit['_id'] = str(response_fruit['_id'])
            serialized_response_fruit.append(response_fruit)
        return serialized_response_fruit

    def find_disease_by_name(self, query: str):
        consulta = {
            'scientific_name': {'$regex': query, '$options': 'i'}
        }
        response_fruits = fruit_fungal_disease_repository.find_fruit_disease_by_consult(consulta)
        if response_fruits is None:
            return []
        serialized_response_fruit = []
        for response_fruit in response_fruits:
            response_fruit['_id'] = str(response_fruit['_id'])
            serialized_response_fruit.append(response_fruit)
        return serialized_response_fruit

    def find_fruit_deseases_by_id(self, fruit_diseases_id: str):
        fruit_diseases = fruit_fungal_disease_repository.find_fruit_diseases_by_id(fruit_diseases_id)
        if fruit_diseases is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Response question with id {fruit_diseases_id} not found"
            )
        fruit_diseases['_id'] = str(fruit_diseases['_id'])
        return fruit_diseases
