from abc import ABCMeta, abstractmethod

class IBookService(metaclass=ABCMeta):
    @abstractmethod
    def get_books(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_book(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    def create_book(self, book):
        raise NotImplementedError
    
    @abstractmethod
    def update_book(self, id:int, new_book):
        raise NotImplementedError
    
    @abstractmethod
    def delete_book(self, id:int):
        raise NotImplementedError    
    
    @abstractmethod
    def get_book_by_Title(self, title:str):
        raise NotImplementedError 
    
    @abstractmethod
    def get_book_contains_Title(self, title:str):
        raise NotImplementedError 
    
    @abstractmethod
    def get_book_contains_autor(self, autor:str):
        raise NotImplementedError    