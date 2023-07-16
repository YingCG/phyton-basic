# Boolean


# Tuples -- not an array. see the bracket. It can store mix datatype
#  here you cant assign new value to tuple. 
# t = (1,2,3, 'a', True, 123)
# print(t)

# t[3] = 'New'
# print(t)
#above code will come out error, here we can use list instead. 
t = [1,2,3, 'a', True, 123]
print(t)

t[3] = 'New'
print(t)

# Sets -- this is unorder, rembmer this is not sorted!
x = set()
x.add(4)
x.add(4)
x.add(0.98)
x.add(4)
print(x)

converted = set([8,1,1,1,63,21, True, 'ghkdfuyasdf'])
print(converted)