def add(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a + b
    raise TypeError('Arguments must be numbers.')