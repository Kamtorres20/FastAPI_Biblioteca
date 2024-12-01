import os
import sys
sys.path.append(f'{os.path.dirname(__file__)}/../app')
from db import PostgreSQL
from models import Book
from pytest_mock import MockerFixture
from repositories import BookRepository
from schemas import UpdateBookSchema


class TestBookRepository:
    def set_config(self, mocker: MockerFixture, mock_book_data) -> None:
        self.book = mock_book_data
        self.books = [self.book for _ in range(5)]
        self.db_factory = mocker.MagicMock(PostgreSQL)



    def test_get_games(self, mocker: MockerFixture, mock_book_data) -> None:
        self.set_config(mocker,mock_book_data)

        self.db_factory.return_value.__enter__.\
        return_value.get_session.\
        return_value.exec.\
        return_value.all.\
        return_value = self.books


        book_repository = BookRepository(self.db_factory)
        books = book_repository.get_books()

        assert isinstance(books, list)


            