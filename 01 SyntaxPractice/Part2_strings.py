print("   /|")
print("  / |")
print(" /  |")
print("/___|")

mystring = 'abcdef'
print(mystring[-1])
print(mystring[3])

# -- add : to start from till the end -- #
print(mystring[2:])

# -- Slicing : stop before index 3 -- #
print(mystring[:3])

# -- Slicing : from index 2 up to index5(but not including 5) -- #
print(mystring[2:5])

# -- get everything : or :: --#
hello = 'hello mashmarrow'
print(hello[:])
print(hello[::])

# -- skip number : or :: --#
print(hello[::1]) #this get everything
print(hello[::2]) #skip after 1
print(hello[::3]) #skip after 2

# build in method to string
sentence = input("What it the plan for tonight?")
s = sentence.upper()
print(s)

t=sentence.capitalize()
print(t)

x = sentence.split()
print(x)

y = sentence.split('e')
print(y)

# print Formatting
a = "Insert another string here: {} ".format(input("How are you feeling?"))
print(a)
# b = "Item one: {} Item Two: {}".format("dog","cat")
# same below, but more dynamic as order doesn't matter anymore
b = "Activity: {x} Hobby: {y}".format(x=(input("what did you do during the weekend: ")),y=(input("your hobby: ")))
print(b)