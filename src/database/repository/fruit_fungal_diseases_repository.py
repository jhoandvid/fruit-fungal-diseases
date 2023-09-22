from src.entity.fruit_fungal_diseases import FruitFungalDisease
from src.database.config.collection import get_collection
from fastapi import HTTPException, status

collection_fruit_disease = get_collection("fruit_fungal_disease")


class FruitFungalDiaseaseRepository:

    def create_fruit_fungal_diasease(self, fruit_fungal_disease: FruitFungalDisease):
        try:
            collection_fruit_disease.insert_one(fruit_fungal_disease)
            return {"ok": True, "msg": "Los datos fueron guardados"}
        except HTTPException as e:
            print("Ocurrio un error")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ocurrio un error comuniquese ocn el adminstrador"
            )

    def find_fruit_fungal_disease(self):
        try:
            response_fruit_disease = collection_fruit_disease.find()
            return response_fruit_disease
        except HTTPException as e:
            print(f'Ocurrio un error {e}')
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ocurrio un error comuniquese con el administrador"
            )
    def find_fruit_disease_by_consult(self, consulta):
        try:
            response_fruit_disease = collection_fruit_disease.find(consulta)
            return response_fruit_disease
        except HTTPException as e:
            print(f'Ocurrio un error {e}')
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ocurrio un error comuniquese con el administrador"
            )




