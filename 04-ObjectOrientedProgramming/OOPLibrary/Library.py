from Book import Book
from User import User


class Library:
    bookcollection = []
    members = []

    # constructor
    def __init__(self, listofBooks):
        # add some dummie product
        # newBook = Book(0001, "S.M.L.XL", True)
        self.availableBooks = listofBooks

    # Method 1: display all book
    def displayAvalablebooks(self):
        if len(self.availableBooks) == 0:
            print("No Books")
        else:
            print("The books we have in our bookclub are: ")
            for book in self.availableBooks:
                print(book)

    # Method 2: Borrow book
    def borrowBook(self, members, book):
        self.user = members
        if book in self.availableBooks:
            self.availableBooks.remove(book)
            print("Confirm Check out: " + book)

    # Method 2: Add a book
    def addBook(self, book):
        self.availableBooks.append(book)
        print(f"{book} is added to the collection")
