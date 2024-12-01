import uvicorn
from container import AppContainer
from fastapi import FastAPI
from models.book import Book
from routes import router
from sqlmodel import SQLModel

def on_startup():
    AppContainer.init()
    SQLModel.metadata.create_all(AppContainer.db_engine())
   
tags = [
    {
        'name': 'API Biblioteca',
        'description': 'Prueba Tecnica para Desarrollador Backend Python'
    }
]

app = FastAPI(
    title='Biblioteca',
    summary='CRUD biblioteca',
    description='Gestionar una pequeña biblioteca',
    openapi_tags=tags,
    on_startup=[on_startup]
)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')