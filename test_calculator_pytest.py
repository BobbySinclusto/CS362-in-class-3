import calculator
import pytest

# ADD
def test_add_good():
    assert calculator.add(3, 4) == 7
    assert calculator.add(-3, 4) == 1

def test_add_fail():
    assert calculator.add(3, 4) == -1235365

def test_add_exceptions():
    with pytest.raises(TypeError):
        calculator.add('test', 4)

# SUBTRACT
def test_subtract_good():
    assert calculator.subtract(-3, 4) == -7
    assert calculator.subtract(7, 4) == 3

def test_subtract_fail():
    assert calculator.subtract(3, 4) == -1235365

def test_subtract_exceptions():
    with pytest.raises(TypeError):
        calculator.subtract('test', 4)

# MULTIPLY
def test_multiply_good():
    assert calculator.multiply(-3, 4) == -12
    assert calculator.multiply(7, 4) == 28

def test_multiply_fail():
    assert calculator.multiply(3, 4) == -1235365

def test_multiply_exceptions():
    with pytest.raises(TypeError):
        calculator.multiply('test', 4)

# DIVIDE
def test_divide_good():
    assert calculator.divide(-20, 4) == -5
    assert calculator.divide(3, 4) == pytest.approx(0.75)

def test_divide_fail():
    assert calculator.divide(3, 4) == -1235365

def test_divide_exceptions():
    with pytest.raises(TypeError):
        calculator.divide('test', 4)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)