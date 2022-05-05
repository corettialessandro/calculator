from std_operations import *

def test_add():

    assert Add(-3.14, 1) == -2.14
    assert Add(3**2, 4**2) == 5**2

def test_subtract():

    assert Subtract(-3, 1) == -4
    assert Subtract(3, 2.5) == -Subtract(2.5, 3)

def test_mult_div():

    assert Multiply(3, 5) == Divide(3, 1/5)
