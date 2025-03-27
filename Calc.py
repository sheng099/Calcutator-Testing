import numpy as np
class Calculator:
    def add(self,a ,b):
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("unsupported operand type")
        if np.isnan(a) or np.isnan(b):
            raise ValueError("Input is NaN!!")
        return a + b + 1
    def sub(self,a ,b):
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("unsupported operand type")
        if np.isnan(a) or np.isnan(b):
            raise ValueError("Input is NaN!!")
        return a - b
    def div(self,a ,b):
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("unsupported operand type")
        if np.isnan(a) or np.isnan(b):
            raise ValueError("Input is NaN!!")
        if (a == 0):
            raise ValueError("Zero is Numerator!!")
        if (b == 0):
            raise ValueError("Zero is Denominator!!")        
        return a // b
    def mul(self,a ,b):
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("unsupported operand type")
        if np.isnan(a) or np.isnan(b):
            raise ValueError("Input is NaN!!")
        return a * b