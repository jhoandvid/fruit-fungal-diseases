from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException, status
from src.utils.jwt_manager import validate_token
from src.database.repository.auth_repository import AuthRepository

auth_repository = AuthRepository()


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        print(data)
        user = auth_repository.find_one_user_by_id(data["_id"])
        if user is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credencials invalid")
        request.state.user_id = user["_id"]
        return user
