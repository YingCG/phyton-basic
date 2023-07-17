fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")

# ####################################################
# # Get the average height in the class

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# totalHeight = 0
# count = 0
# for h in student_heights:
#     totalHeight += h
#     count += 1

# print(totalHeight)
# print(count)
# print(totalHeight / count)

# ####################################################

# # Get the hightest score in the class

# # 78 65 89 86 55 91 64 89
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# highestScore = 0
# for score in student_scores:
#     if score > highestScore:
#         highestScore = score
# print(f"The highest score in the class is: {highestScore}")



# ####################################################

# For loop in range
# for number in range(1,10):
#    print(number)

# total = 0
# for number in range(1,11,2):
#    total += number

# print(total)

# a program that calculates the sum of all the even numbers from 1 to 100. 
totalEven = 0
for num in range(2,101,2):
    totalEven += num
print(totalEven)

# same
total2 = 0
for num2 in range(1,101):
    if num2 % 2 == 0:
        total2 += num2
print(total2)
