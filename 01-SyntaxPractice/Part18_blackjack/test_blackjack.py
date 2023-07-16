import unittest
from blackjack import drawOnecard

class TestFizzBuzz(unittest.TestCase):
    def test_getBuzzIn5(self):
        # setup
        self.testValue = "Q"
        # action
        result = drawOnecard(self.testValue)
        self.assertEqual(result, "Q")

if __name__ == "__main__":
    unittest.main()
