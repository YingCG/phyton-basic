## Problem 1 ##
s ='django'

#use indexing to print out the following
# 'd'
print(s[0])

# 'o'
print(s[-1])

# 'djan'
print(s[:4])

# 'jan'
print(s[1:4])

# 'go'
print(s[4:])

# Use indexing to reverse the string
print(s[::-1])

###################
## Problem 2 ##

# Given this nested list:
item = [3,7,[1,4,'hello']]

# Reassign 'hello' to be 'goodbye'
item[2][2] = 'Goodbye'
print(item)


###################
## Problem 3 ##

#using keys and indexing, grab the 'hello' from the following dictionaries

d1 = {'simple_key' : 'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1' : [{'next_key':['there are a few layer',['hello']]}]}
print(d3['k1'][0]['next_key'][1][0])


###################
## Problem 4 ##

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,1,12,2,2,2,3,3,3]
unique_key = set(mylist)
print(unique_key)

###################
## Problem 5 ##
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is {a} and he is {b} years old.".format(a=age, b=name))

