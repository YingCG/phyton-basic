def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            # not a prime
            is_prime = False
        # Is prime number
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
            