from app.exceptions import IsNoNumeric, IsEmptyString, IsTextSizeExceed

class Book():

    """
    This class implements the book object.

    :insert_library: Add book to database
    :change_name: Change book name in db
    :change_author: Change book author in db
    :change_year: Change book yaer in db
    """

    def __init__(self, name:str, author:str, year:int, id=None) -> None:
        self._name = self.__isEmptyString(name)
        self._author = self.__isEmptyString(author)
        self._year = self.__isNumeric(year)
        self.id = id

    def __str__(self) -> str:
        return f"Name: {self._name}, author: {self._author}, Year: {self._year}"

    def __isNumeric(self, string:str) -> int:
        if str(string).isdigit():
            return int(string)
        else:
            raise IsNoNumeric("The year of the book must be a number")
        
    def __isEmptyString(self, string) -> str:
        if string.strip() == "":
            raise IsEmptyString("Passed parameters must not be empty")
        else:
            if len(string) <= 80:
                return string
            else:
                raise IsTextSizeExceed("Field text is limited to 80 characters, do not exceed the limit")

    def insert_ilbrary(self, db) -> bool:
        result = db.execute(
                    """
                    INSERT INTO library(name, author, year) VALUES(?,?,?)
                    """,
                    (
                        self._name,
                        self._author,
                        self._year
                    )
                )
        if result:
            return True
        else:
            return False
        
    def change_name(self, db, name) -> bool:
        if self.id != None:
            db.execute("UPDATE library SET name = ? WHERE id = ?", (self.__isEmptyString(name), self.id))
            self._name = name
            return True
        else:
            return False
        
    def change_author(self, db, author) -> bool:
        if self.id != None:
            db.execute("UPDATE library SET author = ? WHERE id = ?", (self.__isEmptyString(author), self.id))
            self._author = author
            return True
        else:
            return False
        
    def change_year(self, db, year) -> bool:
        if self.id != None:
            db.execute("UPDATE library SET year = ? WHERE id = ?", (self.__isNumeric(year), self.id))
            self._year = year
            return True
        else:
            return False