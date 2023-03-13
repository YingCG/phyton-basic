#Problem 1

# Given a list of integers, return True if the sequence of numbers 1,2,3
# appears in the list somewhere.

# For example:
# arrayCheck([1,1,1,2,3,1]) -> True
# arrayCheck([1,1,2,4,1]) -> False
# arrayCheck([1,2,1,2,3,1]) -> True
from itertools import count


def array_check(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

print(array_check([1,2,1,2,3,1]))
print(array_check([1,2,1,4,3,1]))

####################################
#Problem 2

# Given a string, return a new string mode of every other character starting 
# wir=th the first, so 'Hello" yields "Hlo"

# For example:

# stringBits('Hello') -> 'Hlo'
# stringBits('Hi') -> 'H
# stringBits('Heeololeo') -> "Hello"

def stringbits(mystring):
    result = ''

    for i in range(len(mystring)):
        if i%2 == 0:
            result = result + mystring[i]
    
    return result

print(stringbits('Hello') )
print(stringbits('Hi') )
print(stringbits('Heeololeo') )

####################################
#Problem 3

# Given two string, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be 'case sensitive').

# Note: s.Lower() returns the lowercase version of a string.
#
# Examples:
# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True

# one way
def end_other(a, b):
    a = a.lower()
    b = b.lower()

    return(b.endswith(a) or a.endswith(b))

# one algorithm way
def end_check(c, d):
    c = c.lower()
    d = d.lower() 

    return c[-(len(d)):] == d or c == d[-len(c):]
print(end_other('Hiacbc', 'bc')  ) 
print(end_check('Hiacbc', 'bc')  ) 
####################################
#Problem 4

# Give a string, return a string where for every char in the original, there are two chars.

# doubleChar('The') -> 'TThhee'
# doubleChar('AAbb') --> 'AAAAbbbbb'
# doubleChar('Hi-There') -> 'HHii--TThheerree'

def doubleChar(str):
    result = ''
    for char in str:
        result += char * 2
    return result

print(doubleChar('huhu'))

####################################
#Problem 5

# Given 3 int values, a b c, return their sum. However, if any of the values is a teen
# -- in the range 13-19 inclusive -- then that value counts as 0, expect 15 and 16 do not count as teens.
# take in an int value and returns that value fixed for the teen rule.
# In this way, yoy avoid repeating the teen code 3 times (i.e. 'decomposition').
# Design the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
# 
# Examples:
#
# no_teen_sum(1,2,3) -- 6
# no_teen_sum(2, 13, 1) -- 3
# no_teen_sum(2, 1, 14) -- 3

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

# def fix_teen(n):
#     if n in [13, 14, 15, 16, 18, 19]:
#         return 0
#     return n

def fix_teen(n):
    if n > 13 and n < 19 :
        return 0
    return n

print(no_teen_sum(6,2,3))

####################################
#Problem 6

# Return the number of even integers in the given array.
#
# Examples:
# count_evens([2, 1, 2,3 ,4]) --3
# count_even([2, 2, 0]) --3
# count_even([1,3,5]) -- 0

def count_evens(*nums):
    count = 0
    
    for element in nums:
        if element % 2 == 0:
            count += 1
    return count

print(count_evens(2, 1, 2, 3 ,4))
