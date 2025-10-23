import datetime
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import User, UserLogin
from app.core.database import user_collection
from app.utils.auth import create_jwt_token, hash_password, verify_password

router = APIRouter


def register(user: User):
    if user_collection. find_one({'email': user.email}):
        raise HTTPException(status_code=400, detail='User already exists')

    user.password = hash_password(user.password)
    user_collection.insert_one(user.model_dump())
    return {'message': 'User registeres succesfully',
            'User': user
            }


def login(credentials: UserLogin):
    user = user_collection.find_one({'email': credentials.email})
    if not user or not verify_password(credentials.password, user['password']):
        raise HTTPException(status_code=401, detail='Invlaid credentials')

    token = create_jwt_token(user['email'])
    return {'access_token': token, 'token_type': 'Bearer'}
