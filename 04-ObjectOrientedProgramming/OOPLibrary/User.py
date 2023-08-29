class User:
    user_Id = 0000
    user_name = None
    listOfBooks = []

    # Constructor
    def __init__(self, name):
        self.user_name = name
        self.listOfBooks = []

    # method
    def displayAccountInfo(self):
        print("You have borrow book: ")
        for book in self.listOfBooks:
            print(book)

    # method
    def checkAccountInfo(self, name):
        self.user_name = name
        print("====================Account Info =======================")

        print("Name: " + self.user_name)
        print("Borrowed book: ")
        for book in self.listOfBooks:
            print(book)
