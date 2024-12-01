import os
import sys
import pytest
from pytest_mock import MockerFixture

sys.path.append(f'{os.path.dirname(__file__)}/../app')

@pytest.fixture
def mock_book_data(mocker: MockerFixture):
    from models import Book

    mock_book = mocker.Mock(Book)
    mock_book.id = 1
    mock_book.titulo = 'La maria'
    mock_book.autor = 'Camilo'
    mock_book.anoPublicacion = 1999
    mock_book.isbn = 'AASDSA89AS5DAS'

    return mock_book