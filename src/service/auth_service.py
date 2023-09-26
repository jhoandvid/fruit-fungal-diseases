from fastapi import HTTPException, status
from src.entity.auth_entity import UserLogin
from src.database.repository.auth_repository import AuthRepository
from src.utils.bycript_password import verify_password, get_hashed_password
from src.utils.jwt_manager import create_token
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
        del new_user['password']
        token = create_token({"_id": new_user['password']})
        return {"user": new_user, "token": token}

    def login(self, user: UserLogin):
        user_db = auth_repository.find_one_user(user.email)

        if user_db is None or not verify_password(user.password, user_db["password"]):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Incorrect email or password"
            )
        del user_db['password']
        token = create_token({"_id": user_db["_id"]})
        return {"user": user_db, "token": token}
