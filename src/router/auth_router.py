from fastapi import APIRouter, Request
from src.entity.auth_entity import User, UserLogin
from src.service.auth_service import AuthService

auth_router = APIRouter()

auth_service = AuthService()


@auth_router.post("/user/signup", tags=["Auth"], description="create a new user")
def create_user(user: User):
    return auth_service.create_user(user)


@auth_router.post("/user/login", tags=["Auth"], description="User login")
def login(user: UserLogin):
    return auth_service.login(user)


@auth_router.post("/user/validate", tags=["Auth"], description="User login")
def login(token: str):
    return auth_service.validate_token(token)
