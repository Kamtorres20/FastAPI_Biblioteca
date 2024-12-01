from typing import Optional
from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):

    id : Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    autor: str
    anoPublicacion: str
    isbn: str


