from math_series import __version__

from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_fibonacci_four():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected


def test_lucas_one():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_two():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_lucas_three():
    actual = lucas(9)
    expected = 76
    assert actual == expected


def test_sum_series_one():
    actual = sum_series(9)
    expected = 34
    assert actual == expected


def test_sum_series_two():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected


def test_sum_series_three():
    actual = sum_series(9, 2, 1)
    expected = 76
    assert actual == expected


def test_sum_series_four():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected


def test_sum_series_five():
    actual = sum_series(6)
    expected = 8
    assert actual == expected
