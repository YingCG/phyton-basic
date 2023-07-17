def fizzBuzz(x):
    if x % 15 == 0:
        return 'FizzBuzz'
    # if x == 3:
    #     return 'Fizz'
    # if x == 5:
    #     return 'Buzz'
    if x % 3 == 0:
        return 'Fizz'
    if x % 5 == 0:
        return 'Buzz'
    return x

def fizzBuzz(x):
    if x % 3 == 0 or x % 5 == 0:
        result = ''

        if x % 3 == 0:
            result += 'Fizz'

        if x % 5 == 0:
            result += 'Buzz'
    else:
        result = x
        
    return result


if __name__ == '__main__':
    print(fizzBuzz(3))
