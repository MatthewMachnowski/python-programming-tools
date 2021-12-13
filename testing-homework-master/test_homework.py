import pytest
from py.error import EEXIST
from homework import take_from_list


def test_recreate_directory_exception(tmpdir):
    (tmpdir / "test").mkdir()
    with pytest.raises(EEXIST):
        (tmpdir / "test").mkdir()


@pytest.mark.parametrize("lst", list(range(1, 20)))
@pytest.mark.parametrize("indices", "1, 9")
def test_indices_type(lst, indices):
    with pytest.raises(ValueError, match="Indices should be integer or list of integers, not <class 'str'>"):
        take_from_list(lst, indices)


@pytest.mark.parametrize("lst", list(range(1, 20)))
@pytest.mark.parametrize("indices", [1, 3, 5, 6, 26, 6, 7, 3, 9])
def test_indices_type(lst, indices):
    with pytest.raises(ValueError, match="Index 26 is to big for list of length 9"):
        take_from_list(lst, indices)


@pytest.mark.parametrize("lst", list(range(20)))
@pytest.mark.parametrize("indices", list(range(20)))
def test_take_from_list(lst: int, indices: int):
    assert take_from_list([], []) == []
    assert take_from_list([1, 4, 9, 15], []) == []
    assert take_from_list([2], 0) == [2]
    assert take_from_list([2, 8], [-1]) == [8]
    assert take_from_list([2, 8], -2) == [2]
