import unittest
import calculator

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)

    def test_substract(self):
        self.assertEqual(calculator.substract(3,3),0)    
        self.assertEqual(calculator.substract(-3,3),0)    
        self.assertEqual(calculator.substract(-3,-3),-6)    
        
if __name__ == '__main__':
    unittest.main()
