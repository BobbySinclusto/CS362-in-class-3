def add(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a + b
    raise TypeError('Arguments must be numbers.')

def subtract(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a - b
    raise TypeError('Arguments must be numbers.')

def multiply(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a * b
    raise TypeError('Arguments must be numbers.')

def divide(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if b != 0:
            return a / b
        raise ZeroDivisionError('Cannot divide by Zero.')
    raise TypeError('Arguments must be numbers.')