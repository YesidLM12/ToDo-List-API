from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings


pwd_context = CryptContext(schemes=['bcrypt'], bcrypt__ident="2b", deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


def hash_password(password: str) -> str:
    password = str(password).strip()
    encoded = password.encode('utf-8')
    
    if len(encoded) > 72:
        encoded = encoded[:72]
        password = encoded.decode('utf-8', errors='ignore')
        
    try:
        hashed = pwd_context.hash(password)
        print('hash generado correctamente')
        return hashed
    except Exception as e:
        print('Error durante el hash: ', e)
        raise

    


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_jwt_token(email: str) -> str:
    now = datetime.utcnow()
    expire = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
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
