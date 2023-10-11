class User:
    user_Id = 0000
    user_name = None
    listOfBooks = []

    # Constructor
    def __init__(self, name):
        self.user_name = name
        self.listOfBooks = []

    # method
    def checkAccountInfo(self):
        print("====================Account Info =======================")

        print("Name: " + self.user_name)
        print("Borrowed book: ")
        for book in self.listOfBooks:
            print(book)

    def addBook(self, book):
        self.listOfBooks.append(book)


    def removeBook(self, book):
        self.listOfBooks.remove(book)