# Can I call FizzBuzz
import unittest
import fizzbuzz
# Get '1' when I pass in 1
# Get '2' when I pass in 2
# Get "Fizz" when I pass in 3
# Get "Buzz" when I pass in 5
# Get "Fizz" when I pass in 6 (a multiple of 3)
# Get "Buzz" when I pass in 6 (a multiple of 5)
# Get "FizzBuzz" when I pass in 15 (a multiple of 3 and 5)


class TestFizzBuzz:
    def test_canCallFizzBuzz(self):
        # setup
        self.testValue = 1

        # action
        result = fizzbuzz(self.testValue)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
