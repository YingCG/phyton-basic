# # Greter than
# 1.1 > 1
# # Less Than
# 1 < 1.1
# # Equality -->python automatic check data type
# 1 == 1
# 1 == "1"

# # AND | OR
# (1 > 2) and (2 < 3)
# (1 > 2) or (2 < 3 )

# IF Else -indent space is important
if 1 < 2:
    if 2 < 3:
        print("True!")

if 3 < 6:  # this line have to go true before it continue
    print("First Block")
    if 20 > 3:
        print("Second Block")

if 1 > 2:
    print("Hello")
elif 3 == 3:
    print("elif ran")
else:
    print("last")

# For Loops
seq = [1, 2, 3, 4, 5, 6]

for jelly in seq:
    print(jelly)

cafe = {"coffee": 1, "bread": 2, "muffin": 3}
for item in cafe:
    print(item)

for k in cafe:
    print(k)
    print(cafe[k])

mypairs = [(1, 2), (3, 4), (5, 6)]

for item in mypairs:
    print(item)

for item1, item2 in mypairs:
    print(item1)
    print(item2)

for tup1, tup2 in mypairs:
    print(tup2)
    print(tup1)

    # While Loops
    print("")
    print("While loops")

i = 1
while i < 5:
    print("i is: {}".format(i))
    i = i + 1

# range
numbers = list(range(0, 5))
print(numbers)

for things in range(10):
    print(things)

# List Comprehension
x = [1, 2, 3, 4]
out = []
for num in x:
    out.append(num**2)  # power of 2

print(out)

square = [num**2 for num in x]
print(square)


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Ticket price: $5")
    elif age <= 18:
        bill = 7
        print("Ticket price: $7")
    else:
        bill = 12
        print("Ticket price: $12")
    photo = input("Do you want a photo taken> Y or N.")

    if photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


"""
This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400
"""

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400:
            print("Leap year")
        else:
            print("Not a Leap year")
    else:
        print("Leap year")
else:
    print("Not a Leap year")
