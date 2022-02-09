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
        print('True!')

if 3 < 6: # this line have to go true before it continue
    print('First Block')
    if 20 > 3:
        print("Second Block")

if 1>2:
    print('Hello')
elif 3 ==3 :
    print('elif ran')
else: 
    print('last')

# For Loops
seq = [1, 2, 3, 4, 5, 6]

for jelly in seq:
    print(jelly)

cafe ={"coffee": 1, "bread": 2, "muffin":3}
for item in cafe:
    print(item)

for k in cafe:
    print(k)
    print(cafe[k])

mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)

for (item1, item2) in mypairs:
    print(item1)
    print(item2)

for tup1, tup2 in mypairs:
    print(tup2)
    print(tup1)   

# While Loops
    print('')   
    print("While loops")   

i = 1
while i < 5:
    print("i is: {}".format(i))
    i = i +1

# range
numbers = list(range(0,5))
print(numbers)

for things in range(10):
    print(things)

# List Comprehension
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2) #power of 2

print(out)

square = [num**2 for num in x]
print(square)