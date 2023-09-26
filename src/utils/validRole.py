from fastapi import Request, HTTPException, Depends
from src.utils.jwt_bearer import JWTBearer
from src.service.auth_service import AuthService

auth_service = AuthService()


class ValidRole:
    def __init__(self, allowed_roles: list):
        self.allowed_roles = allowed_roles

    def __call__(self, request: Request, user=Depends(JWTBearer())):
        if user['role'] not in self.allowed_roles:
            raise HTTPException(status_code=403, detail=f"Forbidden, role {user['role']} not valid")
