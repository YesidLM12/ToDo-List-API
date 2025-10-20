from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import tasks_routes
import uvicorn

from backend.app.api.routes import auth_routes


app = FastAPI(title='API with FastAPI and MongoDB')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(tasks_routes.router, prefix='/task', tags=['tasks'])
app.include_router(auth_routes.router, prefix='/auth', tags=['auth'])

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, log_level='info')
