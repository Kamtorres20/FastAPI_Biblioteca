from sqlmodel import Session,select
from schemas import BookSchema
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