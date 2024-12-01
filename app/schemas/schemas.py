from typing import Optional
from pydantic import BaseModel


class BookSchemaIn(BaseModel):
    titulo: str
    autor: str
    anoPublicacion: int
    isbn: str

class BookSchema(BookSchemaIn):
    id: int

class UpdateBookSchema(BaseModel):
    titulo: Optional[str]=None
    autor: Optional[str]=None
    anoPublicacion: Optional[int]=None
    isbn: Optional[str]=None
