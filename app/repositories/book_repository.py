from sqlmodel import Session,select
from schemas import BookSchema,UpdateBookSchema
from models import Book

class BookRepository:
    def __init__(self, session_factory: Session):
        self.session_factory = session_factory

    def get_books(self):
        with self.session_factory() as db:
            session: Session = db.get_session()
            statement = select(Book)
            return session.exec(statement).all()
        
    def get_book(self, id:int):
        with self.session_factory() as db:
            session: Session = db.get_session()
            statement = select(Book).where(Book.id == id)
            return session.exec(statement).one_or_none()      
        
    def create_book(self, book:BookSchema):
        with self.session_factory() as db:
            session: Session = db.get_session()
            session.add(Book(**book.model_dump()))
            session.commit()
            return True

    def get_book_by_Title(self, title:str):
        with self.session_factory() as db:
            session: Session = db.get_session()
            statement = select(Book).where(Book.titulo == title)
            return session.exec(statement).one_or_none()    

    def get_book_contains_Title(self, title:str):
        with self.session_factory() as db:
            session: Session = db.get_session()
            statement = select(Book).where(Book.titulo.ilike(f"%{title}%"))
            return session.exec(statement).all()

    def get_book_contains_autor(self, autor:str):
        with self.session_factory() as db:
            session: Session = db.get_session()
            statement = select(Book).where(Book.autor.ilike(f"%{autor}%"))
            return session.exec(statement).all()    

    def update_book(self, id:int, book_new:UpdateBookSchema):
        with self.session_factory() as db:
            session: Session = db.get_session()
            statement = select(Book).where(Book.id == id)
            existing_book = session.exec(statement).one_or_none()   
            
            if book_new.titulo is not None:
                existing_book.titulo = book_new.titulo
            if book_new.autor is not None:
                existing_book.autor = book_new.autor
            if book_new.anoPublicacion is not None:
                existing_book.anoPublicacion = book_new.anoPublicacion
            if book_new.isbn is not None:
                existing_book.isbn = book_new.isbn
            
            session.commit()
            return True                            

    def delete_book(self, id:int):
        with self.session_factory() as db:
            session: Session = db.get_session()
            statement = select(Book).where(Book.id == id)
            existing_book = session.exec(statement).one_or_none()  
            session.delete(existing_book)
            session.commit()
            return True                            