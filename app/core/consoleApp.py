from app.core.database import SQLiteDatabase
from app.types.book import Book
from app.types.bookgenerator import BookGenerator
from app.exceptions import IsNoNumeric, IsEmptyString, IsTextSizeExceed
from colorama import init, Fore, Back, Style

class ConsoleApp:

    """
    A class that implements the interface of the console 
    application and its interaction with the database

    :run: Start App
    :output: Print books list (Extend)
    """

    def __init__(self) -> None:
        self.db = SQLiteDatabase("database.db")

    def __addBook(self) -> None:
        """ Adding a book to the database """
        name = input("\nBook name:")
        author = input("Book author:")
        year = input("Book year:")

        try:
            book = Book(name, author, year)
            result = book.insert_ilbrary(self.db)
            print(Fore.GREEN + f"\n[+] Book add to library\n")

        except IsEmptyString as error:
            print(Fore.RED + f"\n[X] {error}\n")

        except IsNoNumeric as error:
            print(Fore.RED + f"\n[X] {error}\n")

        except IsTextSizeExceed as error:
            print(Fore.RED + f"\n[X] {error}\n")

    def __listBook(self) -> None:
        """ Show listbook """
        books = self.db.execute("SELECT * FROM library")
        self.output(books)

    def __editBook(self) -> None:
        """ Edit Book """
        try:
            book_id = int(input("\nSend book number: "))
            book_data = self.db.execute("SELECT id, name, author, year FROM library WHERE id = ?", (book_id,))

            if book_data:
                id, name, author, year = book_data[0]
                book = Book(name, author, year, id)
                while True:
                    print(f"\nEdit Book ({book}):")
                    print("1. Edit Name")
                    print("2. Edit author")
                    print("3. Edit Year")
                    print("4. Back")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        new_name = input("New name: ")
                        result = book.change_name(self.db, new_name)

                    elif choice == "2":
                        new_author = input("New author: ")
                        result =  book.change_author(self.db, new_author)

                    elif choice == "3":
                        new_year = input("New year: ")
                        result = book.change_year(self.db, new_year)

                    elif choice == "4":
                        print("Backed.\n")
                        break

                    else:
                        print(Fore.YELLOW + "\n[!] Invalid choice. Please select again.\n")

                    if result:
                        print(Fore.GREEN + f"\n[+] Book changed\n")
                    else:
                        print(Fore.RED + f"\n[-] Book didn't change\n")
            else:
                print(Fore.RED + f"\n[X] There is no book with this number.\n")
        except Exception as e:
            print(e)
            print(Fore.RED + f"\n[X] The number must be a number\n")

    def __searchBook(self) -> None:
        """ Search Book """
        while True:
            print(f"\nSearch Books")
            print("1. Search by id: ")
            print("2. Search by book name: ")
            print("3. Search by author: ")
            print("4. Search by year")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                id = input("Send id: ")
                result = self.db.execute("SELECT * FROM library WHERE id = ?", (id,))
                self.output(result)

            elif choice == "2":
                name = input("Send name (regx): ")
                result = self.db.execute('SELECT * FROM library WHERE LOWER(name) LIKE ?', ('%' + name.lower() + '%',))
                self.output(result)

            elif choice == "3":
                author = input("Send author(regx): ")
                result = self.db.execute('SELECT * FROM library WHERE LOWER(author) LIKE ?', ('%' + author.lower() + '%',))
                self.output(result)

            elif choice == "4":
                year = input("Send year: ")
                result = self.db.execute("SELECT * FROM library WHERE year = ?", (year,))
                self.output(result)
                
            elif choice == "5":
                print("Backed.\n")
                break

            else:
                print(Fore.YELLOW + "\n[!] Invalid choice. Please select again.\n")

    def __deleteManager(self) -> None:
        """ Search Book """
        while True:
            print(f"\nDelete Manager (Case sensitive):")
            print("1. Delete by id: ")
            print("2. Delete All book by name: ")
            print("3. Delete All book by author: ")
            print("4. Delete All book by year")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                id = input("Send id: ")
                result = self.db.execute("DELETE FROM library WHERE id = ?", (id,))
                print(Fore.YELLOW + "\n[!] Books delete.\n")

            elif choice == "2":
                name = input("Send name: ")
                result = self.db.execute('DELETE FROM library WHERE name = ?', (name,))
                print(Fore.YELLOW + "\n[!] Books delete.\n")

            elif choice == "3":
                author = input("Send author: ")
                result = self.db.execute('DELETE FROM library WHERE author = ?', (author,))
                print(Fore.YELLOW + "\n[!] Books delete.\n")

            elif choice == "4":
                year = input("Send year: ")
                result = self.db.execute("DELETE FROM library WHERE year = ?", (year,))
                print(Fore.YELLOW + "\n[!] Books delete.\n")
                
            elif choice == "5":
                print("Backed.\n")
                break

            else:
                print(Fore.YELLOW + "\n[!] Invalid choice. Please select again.\n")

    def output(self, books):
        if books:
            books_list = BookGenerator(books)
            print("\nLibrary List:\n")
            for book in books_list:
                print(f"[{book.id}] {book}\n")
        else:
            print(Fore.YELLOW + "\n[!] Books no exists.\n")

    def run(self) -> None:
        """ Application launch """
        while True:
            print("Options:")
            print("1. Add a book")
            print("2. List books")
            print("3. Edit books")
            print("4. Serach books")
            print("5. Delete Manager")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.__addBook()

            elif choice == "2":
                self.__listBook()

            elif choice == "3":
                self.__editBook()

            elif choice == "4":
                self.__searchBook()

            elif choice == "5":
                self.__deleteManager()

            elif choice == "6":
                print("Exiting the application.")
                break

            else:
                print(Fore.YELLOW + "\n[!] Invalid choice. Please select again.\n")