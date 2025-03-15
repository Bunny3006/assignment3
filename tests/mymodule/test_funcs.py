import pytest

from myapp.mymodule.funcs import *


@pytest.mark.easy_operation
def test_add():
    # This test will fail.
    assert add(4, 8) == 12

@pytest.mark.easy_operation
def test_subtract():
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    assert divide(56, 8) == 7

@pytest.mark.easy_operation
def test_calculate_area():
    # Using the square root of 73 as the side length
    side_length = 8.544
    expected_area = 73  # We want the area to be 73
    assert calculate_area(side_length) == pytest.approx(expected_area, rel=1e-2)
