from fastapi.routing import APIRouter
from schemas import BookSchemaIn,UpdateBookSchema
import container
from controllers import BookController


router = APIRouter(prefix='/api/v1')
tags_Search= ["API Biblioteca Consulta"]
tags_Action= ["API Biblioteca Acciones"]

@router.get('/libros', tags=tags_Search)
def Obtener_Libros():
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.get_books()

@router.get('/libro/{id}', tags=tags_Search)
def Obtener_Libro_X_Id(id:int):
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.get_book(id)
    
@router.get('/librosTitulo/{title}', tags=tags_Search)
def Obtener_Libro_X_Titulo(title:str):
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.get_book_title(title)    

@router.get('/librosAutor/{autor}', tags=tags_Search)
def Obtener_Libro_X_Autor(autor:str):
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.get_book_autor(autor)       

@router.post('/libros', tags=tags_Action)
def Crear_Libro(book: BookSchemaIn):
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.create_book(book)

@router.put('/libros/{id}', tags=tags_Action)
def Actualizar_Libro(id:int, new_book:UpdateBookSchema):
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.update_book(id,new_book)

@router.delete('/libros/{id}', tags=tags_Action)
def Eliminar_Libro(id:int):
    with container.AppContainer.scope() as app:
        controller: BookController = app.controllers.book_controller()
        return controller.delete_book(id)