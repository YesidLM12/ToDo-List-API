from fastapi import APIRouter
from app.Controller.auth_controller import login, register
from app.schemas.user_schema import User, UserLogin

router = APIRouter()


@router.post('/register')
def register_user(user: User):
    return register(user)

@router.post('/login')
def login_user(credentials: UserLogin):
    return login(credentials)
