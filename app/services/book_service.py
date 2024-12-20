from .ibook_service import IBookService
from schemas import BookSchemaIn, UpdateBookSchema
from models import book

class BookService:

    def __init__(self, book_repository:IBookService):
        self.book_repository = book_repository

    def get_books(self):
        return self.book_repository.get_books()
    
    def get_book(self, id:int):
        return self.book_repository.get_book(id)
    
    def create_book(self, book:BookSchemaIn):
        return self.book_repository.create_book(book)
    
    def update_book(self, id:int, new_book:UpdateBookSchema):
        return self.book_repository.update_book(id,new_book)    

    def delete_book(self, id:int):
        return self.book_repository.delete_book(id)   

    def get_book_by_Title(self, title:str):
        return self.book_repository.get_book_by_Title(title)      

    def get_book_contains_Title(self, title:str):
        return self.book_repository.get_book_contains_Title(title)     
    
    def get_book_contains_autor(self, autor:str):
        return self.book_repository.get_book_contains_autor(autor)      
    
