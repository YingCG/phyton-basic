from Book import Book
from User import User


class Library:
    bookcollection = []

    # constructor
    def __init__(self, listofBooks):
        # add some dummie product
        # newBook = Book(0001, "S.M.L.XL", True)
        self.bookcollection = listofBooks

    # Method 1: display all book
    def displayAvailablebooks(self):
        if len(self.bookcollection) == 0:
            print("No Books")
        else:
            print("The books we have in our bookclub are: ")
            for book in self.bookcollection:
                print(book)

    # Method 2: Borrow book
    def borrowBook(self, user, book):
        if book in self.bookcollection:
            self.bookcollection.remove(book)
            user.addBook(book)
            print("Confirm Check out: " + book)

    # Method 2: Add a book
    def returnBook(self, user, book):
        self.bookcollection.append(book)
        user.removeBook(book)
        print(f"{book} is added to the collection")
        
