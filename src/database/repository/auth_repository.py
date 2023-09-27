from src.entity.auth_entity import User
from src.database.config.collection import get_collection
from fastapi import HTTPException, status
from bson import ObjectId
user_collection = get_collection('users')


class AuthRepository:
    def create_user(self, user: User):

        try:
            json_user = user.dict()
            user_collection.insert_one(json_user)
            json_user["_id"] = str(json_user['_id'])
            return json_user
        except HTTPException as e:
            print("Error", e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ocurrio un error comuniquese con el adminsitrador"
            )

    def find_one_user(self, email: str):
        try:
            user_db = user_collection.find_one({"email": email})
            if user_db:
                user_db['_id'] = str(user_db['_id'])
            return user_db
        except HTTPException as e:
            print("Error", e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ocurrio un error comuniquese con el adminsitrador"
            )

    def find_one_user_by_id(self, user_id):
        try:
            user_db = user_collection.find_one({"_id": ObjectId(user_id)})
            if user_db:
                user_db['_id'] = str(user_db['_id'])
            return user_db
        except HTTPException as e:
            print("Error", e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ocurrio un error comuniquese con el adminsitrador"
            )