class Book:
    book_Id = 0000
    book_title = None
    book_status = None

    # constructor
    def __init__(self, bookId, title, status=True):
        self.book_Id = bookId
        self.book_title = title
        self.book_status = status

    # method
    def displayBookDetails(self):
        print("Book ID: " + self.book_Id)
        print("Title: " + self.book_title)
        print("Status: " + self.book_status)
