import unittest
from numpy import nan
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    # test add
    def test_add(self):
        add_testcases = {
            (2, 3, 5),
            (-2, 3, 1),
            (2, -3, -1),
            (-2, -3, -5)
        }                 
        calc = Calculator()
        for a, b, expected in add_testcases:
            self.assertEqual(calc.add(a, b), expected)
    def test_add_type(self):
        calc = Calculator()
        with self.assertRaises(TypeError) as context:
            calc.add("abc", 2)
        self.assertEqual(str(context.exception), "unsupported operand type")
        with self.assertRaises(TypeError) as context:
            calc.add(2, 'abc')
        self.assertEqual(str(context.exception), "unsupported operand type")
    def test_add_None(self):
        calc = Calculator()
        with self.assertRaises(ValueError) as context:
            calc.add(nan,2)
        self.assertEqual(str(context.exception), "Input is NaN!!")
        with self.assertRaises(ValueError) as context:
            calc.add(2,nan)
        self.assertEqual(str(context.exception), "Input is NaN!!")
    # test sub
    def test_sub(self):
        sub_testcases = {
            (2, 3, -1),
            (-2, 3, -5),
            (2, -3, 5),
            (-2, -3, 1)
        }                 
        calc = Calculator()
        for a, b, expected in sub_testcases:
            self.assertEqual(calc.sub(a, b), expected)
    def test_sub_type(self):
        calc = Calculator()
        with self.assertRaises(TypeError) as context:
            calc.sub("abc", 2)
        self.assertEqual(str(context.exception), "unsupported operand type")
        with self.assertRaises(TypeError) as context:
            calc.sub(2, 'abc')
        self.assertEqual(str(context.exception), "unsupported operand type")
    def test_sub_None(self):
        calc = Calculator()
        with self.assertRaises(ValueError) as context:
            calc.sub(nan,2)
        self.assertEqual(str(context.exception), "Input is NaN!!")
        with self.assertRaises(ValueError) as context:
            calc.sub(2,nan)
        self.assertEqual(str(context.exception), "Input is NaN!!") 
    # test div
    def test_div(self):
        div_testcases = {
            (2, 3, 0),
            (-2, 3, -1),
            (2, -3, -1),
            (-2, -3, 0),
            (3, 2, 1),
            (-3, 2, -2),
            (3, -2, -2),
            (-3, -2, 1)              
        }
        calc = Calculator() 
        for a, b, expected in div_testcases:
            self.assertEqual(calc.div(a, b), expected)
    def test_div_type(self):
        calc = Calculator()
        with self.assertRaises(TypeError) as context:
            calc.div("abc", 2)
        self.assertEqual(str(context.exception), "unsupported operand type")
        with self.assertRaises(TypeError) as context:
            calc.div(2, 'abc')
        self.assertEqual(str(context.exception), "unsupported operand type")        
    def test_div_None(self):
        calc = Calculator()
        with self.assertRaises(ValueError) as context:
            calc.div(nan,2)
        self.assertEqual(str(context.exception), "Input is NaN!!")
        with self.assertRaises(ValueError) as context:
            calc.div(2,nan)
        self.assertEqual(str(context.exception), "Input is NaN!!")
    def test_div_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError) as context:
            calc.div(0,2)
        self.assertEqual(str(context.exception), "Zero is Numerator!!")
        with self.assertRaises(ValueError) as context:
            calc.div(2,0)
        self.assertEqual(str(context.exception), "Zero is Denominator!!")
    # test mul
    def test_mul(self):
        mul_testcase = {
            (2, 3, 6),
            (2, -3, -6),
            (-2, 3, -6),
            (-2, -3, 6),
            (0, 3, 0),
            (2, 0, 0)
        }
        calc = Calculator()
        for a, b, expected in mul_testcase:
            self.assertEqual(calc.mul(a, b), expected)
    def test_mul_type(self):
        calc = Calculator()
        with self.assertRaises(TypeError) as context:
            calc.mul("abc", 2)
        self.assertEqual(str(context.exception), "unsupported operand type")
        with self.assertRaises(TypeError) as context:
            calc.mul(2, 'abc')
        self.assertEqual(str(context.exception), "unsupported operand type")        
    def test_mul_None(self):
        calc = Calculator()
        with self.assertRaises(ValueError) as context:
            calc.mul(nan,2)
        self.assertEqual(str(context.exception), "Input is NaN!!")
        with self.assertRaises(ValueError) as context:
            calc.mul(2,nan)
        self.assertEqual(str(context.exception), "Input is NaN!!")


    


if __name__ == "__main__":
    unittest.main()