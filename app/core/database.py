import sqlite3

class SQLiteDatabase:

    """ A class that implements an interface for working with sqlite3 database """

    def __init__(self, db_name) -> None:
        """ 
        Database initialization and migration 
        
        :db_name: str
        """
        self.db_name = db_name
        self.conn = None

        self.execute("""
                    CREATE TABLE IF NOT EXISTS library(
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name VARCHAR(80),
                        author VARCHAR(80),
                        year INTEGER
                    )
                    """)

    def connect(self) -> None:
        """ Establishing a connection to the database """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self) -> None:
        """ Closing the connection to the database """
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def execute(self, query, params=()) -> set:
        """ 
        Sending a request to the database

        :query: str
        :params: list 
        """
        try:
            self.connect()
            self.cursor.execute(query, params)
            fetched_data = self.cursor.fetchall()
            self.close()
            return fetched_data if fetched_data != [] else False
        except sqlite3.Error as e:
            print("Error:", e)
            self.close()