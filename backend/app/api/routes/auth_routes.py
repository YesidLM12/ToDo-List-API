from fastapi import APIRouter
from backend.app.Controller.auth_controller import login, register
from backend.app.schemas.user_schema import User, UserLogin

router = APIRouter()


@router.post('/register')
def register_user(user: User):
    return register(user)

@router.post('/login')
def login_user(credentials: UserLogin):
    return login(credentials)
