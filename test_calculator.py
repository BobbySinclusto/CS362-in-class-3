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

    # MULTIPLY
    def test_multiply_good(self):
        self.assertEqual(calculator.multiply(-3, 4), -12)
        self.assertEqual(calculator.multiply(7, 4), 28)
    
    def test_multiply_fail(self):
        self.assertEqual(calculator.multiply(3, 4), -1235365)
    
    def test_multiply_exceptions(self):
        self.assertRaises(TypeError, calculator.multiply, 'test', 4)

    # DIVIDE
    def test_divide_good(self):
        self.assertEqual(calculator.divide(-20, 4), -5)
        self.assertAlmostEqual(calculator.divide(3, 4), 0.75)
    
    def test_divide_fail(self):
        self.assertEqual(calculator.divide(3, 4), -1235365)
    
    def test_divide_exceptions(self):
        self.assertRaises(TypeError, calculator.divide, 'test', 4)
    
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculator.divide, 5, 0)

if __name__ == '__main__':
    unittest.main()