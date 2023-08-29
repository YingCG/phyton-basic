from Library import Library
from User import User

if __name__ == "__main__":
    beachbookclub = Library(["S.M.L.XL", "Deluxe", "Form and object"])
    members = User(["Jerry", "Tom"])

    while True:
        print("===================== LIBRARY MENU =====================")
        print("1. Show all available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Check user account")
        print("5. Exit")
        print("========================================================")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            print("Books currently available are: ")
            beachbookclub.displayAvalablebooks()
        elif user_choice == "2":
            requestedBook = input("Which book are you borrowing? ")
            borrower = input("Username: ")
            beachbookclub.borrowBook(borrower, requestedBook)
            members.listOfBooks.append(requestedBook)
            members.displayAccountInfo()
        elif user_choice == "3":
            returnedBook = input("Which book are you returning? ")
            beachbookclub.addBook(returnedBook)
        elif user_choice == "4":
            userProfile = input("Enter username: ")
            members.checkAccountInfo(userProfile)
        elif user_choice == "5":
            exit()
