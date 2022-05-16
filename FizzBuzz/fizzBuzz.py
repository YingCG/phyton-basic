# def add(x,y):
#     return x + y

def fizzBuzzOne(value):
    """
    Takes a number and return its fizz buzz value
    Arguments:
        value: A number
    Returns:
        Fizz if the nubmer is divisible by 3
        Buzz if the nubmer is divisible by 5
        FizzBuzz if the nubmer is divisible by 3 and 5
        Otherwise, the number as a string
    """
    if value % 3 == 0 and value % 5 == 0:
        return("FizzBuzz")
    elif value % 3 == 0:
        return ("Fizz") 
    elif value % 5 == 0:
        return("Buzz")
    else:
        return str(value)

def fizzBuzzMany(values):
    """
    Looks through all the numbers provided in the list values and return an updated array of fizzbuzz values
    Arguments:
        values: the array
    Returns:
        The array updated
    """
    items = []
    for value in values:
        newValue = fizzBuzzOne(value)
        items.append(newValue)
    return items


def fizzBuzzStar(*values):
    """
    Looks through all the numbers provided in the list values and return an updated array of fizzbuzz values
    Arguments:
        values: the array
    Returns:
        The array updated
    """
    return fizzBuzzMany(values)