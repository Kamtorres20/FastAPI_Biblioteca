import os
import sys
sys.path.append(f'{os.path.dirname(__file__)}/../app')
import pytest
from pytest_mock import MockerFixture
from repositories import BookRepository
from services import BookService

class TestBookService:
    def set_config(self, mocker: MockerFixture, mock_book_data) -> None:
        self.book = mock_book_data
        self.books = [self.book for _ in range(5)]

        self.book_repository = mocker.Mock(BookRepository)
        self.book_repository.get_books.return_value = self.books
        self.book_repository.get_book.return_value = self.book
        self.book_repository.create_book.return_value = True

        self.book_service = BookService(self.book_repository)

    def test_get_books_services(self, mocker: MockerFixture, mock_book_data) -> None:
        self.set_config(mocker,mock_book_data)

        response = self.book_service.get_books()

        assert isinstance(response, list) 
      
