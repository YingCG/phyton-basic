import unittest
from unittest import result
from fizzBuzz import fizzBuzzOne, fizzBuzzMany, fizzBuzzStar

# use case
# Can I call FizzBuzz
# Get "1" when i pass in 1
# Get "2" when i pass in 2
# Get "Fizz" when I pass in 3
# Get "Buzz" when I pass in 5
# Get "Fizz" when I pass in 6(a multiple of 3)
# Get "Buzz" when i pass in 10 (a multiple of 5)
# Get "FizzBuzz" when I pass in 15 (a multiple of 3 and 5)

class TestFizzBuzz(unittest.TestCase):

    # Test1: Can I call FizzBuzz
    def test_canCallFizzBuzz(self):
        return True

    # Test2: Get "1" when i pass in 1
    def test_return1whenPassIn1(self):
        result = fizzBuzzOne(1)
        self.assertEqual(result, "1")

    # Test3: Get "2" when i pass in 2
    def test_return2whenPassIn2(self):
        result = fizzBuzzOne(2)
        self.assertEqual(result, "2")

    # Test4: Get "Fizz" when I pass in 3
    def test_returnFizzWhenPassIn3(self):
        fizz = fizzBuzzOne(3)
        self.assertEqual(fizz, "Fizz")

    # Test5: Get "Buzz" when I pass in 5
    def test_returnBuzzWhenPassIn5(self):
        buzz = fizzBuzzOne(5)
        self.assertEqual(buzz, "Buzz")
    
    # Test6: Get "Fizz" when I pass in 6(a multiple of 3)
    def test_returnFizzWhenMutipleOf3(self):
        fizz = fizzBuzzOne(6)
        self.assertEqual(fizz, "Fizz")

    # Test7: Get "Buzz" when i pass in 10 (a multiple of 5)
    def test_returnFizzWhenMutipleOf5(self):
        buzz = fizzBuzzOne(10)
        self.assertEqual(buzz, "Buzz")

    # Test8: Get "FizzBuzz" when I pass in 15 (a multiple of 3 and 5)
    def test_returnFizzBuzzWhenMutipleOf3and5(self):
        fizzbuzz = fizzBuzzOne(15)
        self.assertEqual(fizzbuzz, "FizzBuzz")

    # Test9: Get array when i pass more than 1 value
    def test_ableToPassInArray(self):
        items = fizzBuzzMany([3, 5, 15, 21, 35, 11])
        self.assertEqual(items, ["Fizz", "Buzz", "FizzBuzz", "Fizz", "Buzz", "11"])

    # Test10: Get separate values when i pass more than 1 value
    def test_ableToPassInMukltipleValues(self):
        items = fizzBuzzStar(3, 5, 15, 21, 35, 11)
        self.assertEqual(items, ["Fizz", "Buzz", "FizzBuzz", "Fizz", "Buzz", "11"])

if __name__ == '__main__':
    unittest.main()