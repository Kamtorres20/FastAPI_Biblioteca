from services import IBookService
from utils import Utils
from schemas import BookSchemaIn,UpdateBookSchema,BookSchema
from fastapi import HTTPException

class BookController:
    def __init__(self, book_service: IBookService) -> None:
        self.book_service = book_service
    
    def get_books(self):
        books = self.book_service.get_books()
        if not books:
            raise HTTPException(status_code=202, detail='No existen Libros en la base de datos')            
        books_mapped = Utils.mapping(books)
        return books_mapped
    
    def get_book(self, id:int):
        book = self.book_service.get_book(id)
        if not book:
            raise HTTPException(status_code=202, detail='Libro no encontrado')
        book_mapped = Utils.mapping(book)
        return {'book': book_mapped}

    def get_book_title(self, title:str):
        book = self.book_service.get_book_contains_Title(title)
        if not book:
            raise HTTPException(status_code=202, detail='No existen Libros en la base de datos con este titulo')
        book_mapped = Utils.mapping(book)
        return {'book': book_mapped}    

    def get_book_autor(self, autor:str):
        book = self.book_service.get_book_contains_autor(autor)
        if not book:
            raise HTTPException(status_code=202, detail='No existen Libros en la base de datos con este autor')
        book_mapped = Utils.mapping(book)
        return {'book': book_mapped}      
    
    def create_book(self, book:BookSchemaIn):
        book_db = self.book_service.get_book_by_Title(book.titulo)
        if book_db:
            raise HTTPException(status_code=202, detail='Libro ya Existe') 
        success = self.book_service.create_book(book)
        if not success:
            raise HTTPException(status_code=500, detail='Error al insertar libro') 
        raise HTTPException(status_code=201, detail='Libro insertado correctamente')    
    
    def update_book(self,id:int, new_book:UpdateBookSchema):
        book_db = self.book_service.get_book(id)
        if not book_db:
            raise HTTPException(status_code=202, detail='No se encontró el libro para actualizar') 
        
        success = self.book_service.update_book(id,new_book)
        if not success:
            raise HTTPException(status_code=500, detail='Error al Actualizar libro') 
        raise HTTPException(status_code=201, detail='Libro Actualizado correctamente') 

    def delete_book(self,id:int):
        book_db = self.book_service.get_book(id)
        if not book_db:
            raise HTTPException(status_code=202, detail='No se encontró el libro para Eliminar') 
        
        success = self.book_service.delete_book(id)
        if not success:
            raise HTTPException(status_code=500, detail='Error al Eliminar libro') 
        raise HTTPException(status_code=201, detail='Libro Eliminar correctamente')     
   