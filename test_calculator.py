import unittest
import calculator

class TestCaseCalculator(unittest.TestCase):
    def test_add_good(self):
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(-3, 4), 1)
    
    def test_add_fail(self):
        self.assertEqual(calculator.add(3, 4), -1235365)

if __name__ == '__main__':
    unittest.main()