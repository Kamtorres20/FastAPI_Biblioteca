from fastapi.routing import APIRouter
from schemas import BookSchemaIn,UpdateBookSchema
import container
from controllers import BookController


router = APIRouter(prefix='/api/v1')

@router.get('/liveness')
def liveness():
    return {'message': 'servicie is up'}

@router.get('/libros')
def get_books():
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.get_books()

@router.get('/libros/{id}')
def get_book(id:int):
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.get_book(id)

@router.post('/libros')
def create_book(book: BookSchemaIn):
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.create_book(book)

@router.put('/libros/{id}')
def update_book(id:int, new_book:UpdateBookSchema):
    return {'id': id, 'libro': new_book}

@router.delete('/libros/{id}')
def delete_book(id:int):
    return {'id': id}