import os
import sys
sys.path.append(f'{os.path.dirname(__file__)}/../app')
from pytest_mock import MockerFixture
from controllers import BookController
from schemas import BookSchema
from services import BookService
from utils import Utils


class TestBookController:
    def set_config(self, mocker: MockerFixture, mock_book_data)-> None:
        self.book = mock_book_data
        self.books = [self.book for _ in range(5)]

        self.book_service = mocker.Mock(BookService)
        self.book_service.get_books.return_value = self.books

        self.book_controller = BookController(self.book_service)

    def test_get_books(self, mocker: MockerFixture, mock_book_data)-> None:
        self.set_config(mocker,mock_book_data)

        def mock_mapping(books):
            mock_data = {'id':1, 'titulo': 'La maria', 'autor': 'Camilo', 'anoPublicacion': 1999, 'isbn': 'AASDSA89AS5DAS'}

            return [BookSchema(**mock_data) for _ in range(2)]
        
        mocker.patch.object(Utils, 'mapping', mock_mapping)

        response = self.book_controller.get_books()

        assert isinstance(response, list) 

    def test_get_book(self, mocker: MockerFixture, mock_book_data)-> None:
        self.set_config(mocker,mock_book_data)

    def test_create_book(self, mocker: MockerFixture, mock_book_data)-> None:
        self.set_config(mocker,mock_book_data)        