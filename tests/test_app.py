import pytest

from myapp.app import multiply_by_two, divide_by_two, calculate_square_area


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    def test_calculate_area(self):
        # Using the square root of 73 as the side length
        side_length = 8.544  # We expect this to give an area of 73
        expected_area = 73  # The expected area
        result = calculate_square_area(side_length)
        assert result == pytest.approx(expected_area, rel=1e-2)  # Use pytest.approx for floating point comparison
