from services.ibook_service import IBookService
from utils.utils import Utils
from schemas.schemas import BookSchemaIn

class BookController:
    def __init__(self, book_service: IBookService) -> None:
        self.book_service = book_service
    
    def get_books(self):
        books = self.book_service.get_books()
        if not books:
            return {'message': 'No existen Libros en la base de datos'}
        books_mapped = Utils.mapping(books)
        return books_mapped
    
    def get_book(self, id:int):
        book = self.book_service.get_book(id)    

        if not book:
            return {'message': 'Libro no encontrado'}
        
        book_mapped = Utils.mapping(book)
        return {'book': book_mapped}
    
    def create_book(self, book:BookSchemaIn):
        book_db = self.book_service.get_book_by_Title(book.titulo)
        if book_db:
            return {'message': 'Libro ya Existe'}
        
        success = self.book_service.create_book(book)

        if not success:
            return {'message': 'Error al insertar libro'}

        return {'message': 'Libro insertado correctamente'}  