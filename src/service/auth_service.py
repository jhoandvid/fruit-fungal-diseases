from fastapi import HTTPException, status
from src.entity.auth_entity import UserLogin
from src.database.repository.auth_repository import AuthRepository
from src.utils.bycript_password import verify_password, get_hashed_password
from src.utils.jwt_manager import create_token, validate_token
from src.entity.auth_entity import User

auth_repository = AuthRepository()


class AuthService:
    def create_user(self, user: User):
        exist_user_db = auth_repository.find_one_user(email=user.email)

        if exist_user_db is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )
        user.password = get_hashed_password(user.password)
        new_user = auth_repository.create_user(user)
        token = create_token({"_id": new_user['_id']})

        response_data = {
            "id": new_user["_id"],
            "email": new_user["email"],
            "name": new_user["name"],
            "role": new_user["role"],
            "createdAt": new_user["createdAt"],
            "token": token
        }
        return response_data

    def login(self, user: UserLogin):
        user_db = auth_repository.find_one_user(user.email)

        if user_db is None or not verify_password(user.password, user_db["password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )

        token = create_token({"_id": user_db["_id"]})
        response_data = {
            "id": user_db["_id"],
            "email": user_db["email"],
            "name": user_db["name"],
            "role": user_db["role"],
            "createdAt": user_db["createdAt"],
            "token": token
        }
        return response_data

    def find_one_user_by_id(self, user_id):
        print(user_id)
        user = auth_repository.find_one_user_by_id(user_id)
        print(user)
        if user is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credencials invalid")
        return user

    def validate_token(self, user_id: str):
        user = self.find_one_user_by_id(user_id)
        token = create_token({"_id": user['_id']})
        response_data = {
            "id": user["_id"],
            "email": user["email"],
            "name": user["name"],
            "role": user["role"],
            "createdAt": user["createdAt"],
            "token": token
        }
        return response_data
