import unittest

def encrypt(message):
    return 0

class TestEncryption(unittest.TestCase):
    # def setUp(self):
    #     self.my_message = ""
    # tests go here
    def test_inputExists(self):
        self.assertIsNone(self.my_message)
    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)
        
    def test_functionRetrunsSomething(self):
        self.assertIsNone(encrypt(self.my_message))
    
if __name__ == "__main__":
    unittest.main()

# Use this instead if using jupyter notebook
# unittest.main(argv=[''], verbosity=2, exit=False)