import pytest

from src.hypot.triangles import sqrt


# test sqrt function
# input = 4, output = 4.0
def test_sqrt():  # must have test_ for pytest
    """Integer output"""
    val = 4
    expected = 2.0
    assert sqrt(val) == expected

def test_2():
    """Floating point output"""
    val = 2
    expected = 1.41421356237
    assert sqrt(val) == pytest.approx(expected, rel=1e-6)  


# test hypotenuse function
