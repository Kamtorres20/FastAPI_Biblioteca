from schemas.schemas import BookSchema

class Utils:
    @classmethod
    def mapping(cls, books):
        if isinstance(books, list):
            return [BookSchema(**book.model_dump()) for book in books]
        return BookSchema(**books.model_dump())