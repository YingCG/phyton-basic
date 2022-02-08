print("   /|")
print("  / |")
print(" /  |")
print("/___|")

mystring = 'agadfau'
print(mystring[-1])
print(mystring[3])

# -- add : to start from till the end -- #
print(mystring[2:])

# -- Slicing : stop before index 3 -- #
print(mystring[:3])

# -- Slicing : from index 2 up to index5(but not including 5) -- #
print(mystring[2:5])

# -- get everything : or :: --#
print(mystring[::])

# -- skip number : or :: --#
print(mystring[::1]) #this get everything
print(mystring[::2]) #skip after 1

# build in method to string
sentence = 'Hello you'
s = sentence.upper()
print(s)

t=sentence.capitalize()
print(t)

x = sentence.split()
print(x)

y = sentence.split('e')
print(y)

# print Formatting
a = "Insert another string here: {} ".format("Insert me!")
print(a)
# b = "Item one: {} Item Two: {}".format("dog","cat")
# same below, but more dynamic as order doesn't matter anymore
b = "Item one: {x} Item Two: {y}".format(x="dog",y="cat")
print(b)