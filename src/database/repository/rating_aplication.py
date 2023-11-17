from src.database.config.collection import get_collection
from fastapi.responses import JSONResponse
from src.entity.raiting_aplication import RatingAplication
from fastapi import HTTPException, status
from bson import ObjectId

collection_rating = get_collection("rating")


class RatingAplicationRepository:

    def create_rating_aplicacion(self, rating_aplication: RatingAplication):
        try:
            new_rating = collection_rating.insert_one(rating_aplication.dict())
            rating_id = str(new_rating.inserted_id)
            response_content = {
                "id": rating_id,
                "rating": rating_aplication.rating,
                "comment": rating_aplication.comment
            }
            return JSONResponse(content=response_content, status_code=201)
        except HTTPException as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Hubo un error, contacte al administrador")

    def find_rating_aplication(self, user_id: str):
        try:
            collection_result = collection_rating.find_one({"user_id": user_id})
            return collection_result
        except Exception as e:
            print(e)
            raise HTTPException(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="There was an error contact the administrator, please try again",
            )

    def update_rating_aplication(self, rating_aplication: RatingAplication):
        try:
            collection_rating.update_one({"user_id": rating_aplication.user_id},
                                                      {"$set": rating_aplication.dict()})

            updated_rating = self.find_rating_aplication(rating_aplication.user_id)
            if updated_rating is not None:
                updated_rating["_id"] = str(updated_rating["_id"])
            return updated_rating
        except Exception as e:
            print(e)
            raise HTTPException(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="There was an error contact the administrator, please try again",
            )
