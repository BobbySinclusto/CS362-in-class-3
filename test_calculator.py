import unittest
import calculator

class TestCaseCalculator(unittest.TestCase):
    # ADD
    def test_add_good(self):
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(-3, 4), 1)
    
    def test_add_fail(self):
        self.assertEqual(calculator.add(3, 4), -1235365)
    
    def test_add_exceptions(self):
        self.assertRaises(TypeError, calculator.add, 'test', 4)
    
    # SUBTRACT
    def test_subtract_good(self):
        self.assertEqual(calculator.subtract(-3, 4), -7)
        self.assertEqual(calculator.subtract(7, 4), 3)
    
    def test_subtract_fail(self):
        self.assertEqual(calculator.subtract(3, 4), -1235365)
    
    def test_subtract_exceptions(self):
        self.assertRaises(TypeError, calculator.subtract, 'test', 4)

if __name__ == '__main__':
    unittest.main()