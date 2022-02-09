mylist = ['a','b','c','d','e']
print(mylist[-1])
print('single collen')
print(mylist[:1])
print(mylist[:3])

print('double collen')
print(mylist[::1])
print(mylist[::3])

print('before reassignment: ')
print(mylist)
mylist[0] = 'New things'
print('after reassignment: ')
print(mylist)

mylist.append('New adventure')
print(mylist)

listtwo = ['apple','banana']
# mylist.append(listtwo)
# print('append array: ')
# print(mylist)

mylist.extend(listtwo)
print('extend array: ')
print(mylist)

item = mylist.pop()
print(mylist)
print(item)

mylist.reverse()
print(mylist)

numberlist = [5, 9,23,1,78]
numberlist.sort()
print(numberlist)

newlist = [1,2,['x','y','s']]
print(newlist[2])
print(newlist[2][2])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0])

#get first index of each col
first_col = [row[0] for row in matrix]
print(first_col)

