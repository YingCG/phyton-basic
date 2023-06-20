# Can I call FizzBuzz
import unittest
from fizzbuzz import fizzBuzz
# Get '1' when I pass in 1
# Get '2' when I pass in 2
# Get "Fizz" when I pass in 3
# Get "Buzz" when I pass in 5
# Get "Fizz" when I pass in 6 (a multiple of 3)
# Get "Buzz" when I pass in 10 (a multiple of 5)
# Get "FizzBuzz" when I pass in 15 (a multiple of 3 and 5)


class TestFizzBuzz(unittest.TestCase):
    # Get '1' when I pass in 1
    def test_canCallFizzBuzz(self):
        # setup
        self.testValue = 1
        # action
        result = fizzBuzz(self.testValue)
        self.assertEqual(result, 1)

    # Get '2' when I pass in 2
    def test_whenPassIn2(self):
        self.testValue = 2
        # action
        result = fizzBuzz(self.testValue)
        self.assertEqual(result, 2)

    # Get "Fizz" when I pass in 3
    def test_getFizzIn3(self):
        # setup
        self.testValue = 3
        # action
        result = fizzBuzz(self.testValue)
        self.assertEqual(result, "Fizz")

    # Get "Buzz" when I pass in 5
    def test_getBuzzIn5(self):
        # setup
        self.testValue = 5
        # action
        result = fizzBuzz(self.testValue)
        self.assertEqual(result, "Buzz")
    
    # Get "Fizz" when I pass in 6 (a multiple of 3)
    def test_getFizzWhenModular3isZero(self):
        self.assertEqual(fizzBuzz(6), 'Fizz')    

    # Get "Buzz" when I pass in 10(a multiple of 5)
    def test_getBuzzWhenModular5isZero(self):
        self.assertEqual(fizzBuzz(10), 'Buzz')

    # Get "FizzBuzz" when I pass in 15 (a multiple of 3 and 5)
    def test_getFizzBuzzWhenModular3and5isZero(self):
        self.assertEqual(fizzBuzz(15), 'FizzBuzz')


if __name__ == "__main__":
    unittest.main()
