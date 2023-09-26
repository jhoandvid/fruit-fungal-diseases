from jwt import encode, decode
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from src.utils.environment.env import setting


def create_token(data: dict):
    expires_delta = datetime.utcnow() + timedelta(days=7)
    data["exp"] = expires_delta
    token: str = encode(payload=data, key=setting.JWT_SECRET_KEY, algorithm=setting.ALGORITHM)
    return token


def validate_token(token: str) -> dict:
    try:
        data: dict = decode(token, key=setting.JWT_SECRET_KEY, algorithms=setting.ALGORITHM)
        return data
    except ExpiredSignatureError as e:
        print(f"Token has expired: {e}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except InvalidSignatureError as e:
        print(f"Error de firma no válida: {e}")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuario no autorizado")
