from fastapi import APIRouter, Request, Depends
from src.entity.auth_entity import User, UserLogin
from src.service.auth_service import AuthService
from src.utils.validRole import ValidRole

auth_router = APIRouter()

auth_service = AuthService()


@auth_router.post("/user/signup", tags=["Auth"], description="create a new user")
def create_user(user: User):
    return auth_service.create_user(user)


@auth_router.post("/user/login", tags=["Auth"], description="User login")
def login(user: UserLogin):
    return auth_service.login(user)


@auth_router.get("/user/validate", tags=["Auth"], description="User login",
                 dependencies=[Depends(ValidRole(['user', 'admin']))])
def login(request: Request):
    user_id = request.state.user_id
    return auth_service.validate_token(user_id)
