import unittest

class TestEncryption(unittest.TestCase):
    # tests go here
    def test_inputExists(self):
        self.assertIsNone(self.my_message)
    
    
if __name__ == "__main__":
    unittest.main()

# Use this instead if using jupyter notebook
# unittest.main(argv=[''], verbosity=2, exit=False)