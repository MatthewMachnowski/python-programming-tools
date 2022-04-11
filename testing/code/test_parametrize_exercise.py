from typing import List

import pytest


def norm(vec: List[float], norm: int):
    return sum(pow(v, norm) for v in vec)


@pytest.mark.parametrize("vec_len", list(range(1, 10)))
@pytest.mark.parametrize("norm_num", list(range(1, 10)))
def test_norm(vec_len, norm_num):
    assert norm([1] * vec_len, norm_num) == vec_len
