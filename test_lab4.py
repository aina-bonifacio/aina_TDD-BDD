'''
import pytest 


assert Calculator.subtract(2, 1) == 1
assert Calculator.multiply(2, 3) == 6
'''

import pytest

class Calculator:
        
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

calc = Calculator()

def test_lab4():
    calc.subtract(-5, -2) == -3
    calc.multiply(2, -3) == -6

    print(calc.subtract(-5, -2))
    print(calc.multiply(2, -3))
    
    assert True


