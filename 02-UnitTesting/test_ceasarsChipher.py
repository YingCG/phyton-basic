import unittest
from caesarsChipher import encrypt
    
    #e.g. zu
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

class TestCeasarsChiper(unittest.TestCase):
    def test_canCallEncrypt(self):
        self.inputText = 'hello'
        self.numToShift = '5'

        result = encrypt(self.inputText, self.numToShift)
        self.assertEqual(result, "hello5")


if __name__ == "__main__":
    unittest.main()