from datetime import datetime, timedelta
from operator import setitem
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_jwt_token(email: str) -> str:
    now = datetime.utcnow()
    expire = now + timedelta(minutes= settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        'sub': email,
        'iat': int(now.timestamp()),
        'exp': int(expire.timestamp()),
    }
    token = jwt.encode(payload, settings.SECRET_KEY,
                       algorithm=settings.ALGORITHM)
    return token


def verify_jwt_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        email = payload.get('sub')
        if email is None:
            raise HTTPException(
                status_code=401, detail='Invalid token: missing email')
        return {'email': str(email)}
    except JWTError:
        raise HTTPException(status_code=401, detail='Invalid or expire token')
