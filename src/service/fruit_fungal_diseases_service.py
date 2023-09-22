from src.entity.fruit_fungal_diseases import FruitFungalDisease
from src.database.repository.fruit_fungal_diseases_repository import FruitFungalDiaseaseRepository

fruit_fungal_disease_repository = FruitFungalDiaseaseRepository()


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




