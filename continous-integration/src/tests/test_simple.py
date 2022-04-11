import pytest

from sample_package import fibonacci, good_data


@pytest.mark.parametrize("num,value", [(1, 1), (3, 3), (9, 55), (11, 144)])
def test_fibonacci(num, value):
    assert fibonacci(num) == value


def test_good_data():
    assert not good_data(0)
    assert good_data(2)
    assert not good_data(7)
