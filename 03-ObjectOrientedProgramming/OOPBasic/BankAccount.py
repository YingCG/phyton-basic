# import datetime
from datetime import date


class BankAccount:
    account_number: None
    account_holder: None
    balance: None
    opening_date: None

    # constructor
    def __init__(self, name, number):
        self.NAME = name
        self.sAVING_aCCONT = number
        self.balance = 50000
        self.opening_date = date.today()

    # saving some dollar
    def deposit(self, dollar):
        self.balance += dollar

    # withdraw
    def withdraw(self, dollar):
        if dollar > self.balance:
            print("Not enough money in the bank")
            return
        self.balance -= dollar

    def display_info(self):
        print("***** Bank Account *****")
        print("account number: ", self.account_number)
        print("account holder ", self.account_holder)
        print("balance: ", self.balance)
        print("opening date: ", self.opening_date)
