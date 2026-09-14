from calulator import *
import pytest


# This is used when you want to run the same test multiple times with different values.
# @ is Python's decorator syntax.
@pytest.mark.parametrize("a , b ,expected", [(2,3,5), (-3 ,1 ,-2)])
# The decorator applies to the immediately following function.
def test_add(a,b,expected):
    assert add(a,b) == expected

def test_multiply():
    assert multiply(9,2) == 18

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

def test_is_even():
    assert is_even(4) is True