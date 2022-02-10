#Problem 1

# Given a list of integers, return True if the sequence of numbers 1,2,3
# appears in the list somewhere.

# For example:
# arrayCheck([1,1,1,2,3,1]) -> True
# arrayCheck([1,1,2,4,1]) -> False
# arrayCheck([1,2,1,2,3,1]) -> True
def array_check(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

print(array_check([1,2,1,2,3,1]))

####################################
#Problem 2

# Given a string, return a new string mode of every other character starting 
# wirth the first, so 'Hello" yields "HLo"

# For example:

# stringBits('Hello') -> 'HLo'
# stringBits('Hi') -> 'H
# stringBits('HeeoloLeo') -> "Hello"