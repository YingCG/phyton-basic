def my_func(param1='default'):
    print('Hello python')

my_func()

def second_func(day = 'Thursday'):
    """
    This is the dockstring
    """
    print('Today is {}'.format(day))

second_func()

def hello():
    return 'hello'

result = hello()
print(result)

def addNum(num1, num2):
    return num1 + num2

add = addNum(3,4)
print(type(add))
print(add)


def add_Number(num1, num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, please enter intergers!"

sum = add_Number(3, 5 )
print(sum)


# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,mylist)
print(list(evens))

# Lambda Expression mean function only use one time, no need to do reuseable function
even_number = filter(lambda num:num%2 == 0,mylist )
print (even_number)
print (list(even_number))

tweet = "Go Sports! #Sports"
result = tweet.split('#')
print(result)

