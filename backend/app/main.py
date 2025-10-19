from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import tasks_routes
import uvicorn


app = FastAPI(title= 'API with FastAPI and MongoDB')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(tasks_routes.router, prefix='/task',tags=['tasks'])

@app.get('/')
def read_root():
    return {'Hello': 'World'}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, log_level='info')
    