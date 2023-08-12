from app.types.book import Book

class BookGenerator:
    """ Generates from a base response to an array of book objects """
    def __init__(self, data_list) -> None:
        self.data_list = data_list

    def __iter__(self) -> list[Book]:
        for data in self.data_list:
            id, name, author, year = data
            yield Book(name, author, year, id)