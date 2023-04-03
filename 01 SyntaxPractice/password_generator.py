import random

print("Welcome to the Python Password Generator!")
letterSet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbolSet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numberSet = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

letterNum = int(input("How many letters would you like in your password?"))
symbolNum = int(input("How many symbols would you like in your password?"))
numberNum = int(input("How many numbers would you like in your password?"))
password = []

for char in range(1, letterNum + 1):
    letter = random.choice(letterSet)
    password += letter

for symb in range(1, symbolNum + 1):
    symbol = random.choice(symbolSet)
    password += symbol

for num in range(1, numberNum + 1):
    password += random.choice(numberSet)

# simply concat the password
# password = "".join(password)
# print(f"Here is your password: {password}")

# below is shuffle the list after the concat
newPassword = ""
random.shuffle(password)
for char in password:
    newPassword += char

print(f"Here is your password: {newPassword}")
