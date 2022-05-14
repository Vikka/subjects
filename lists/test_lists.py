from random import randint

from pytest import mark

from helpers.custom_list import list_


def get_list(result: list):
    assert isinstance(result, list)
    assert len(result) >= 1
    assert result[-1] is ...
    assert result.count(...) == 1
    result.pop()
    return list(result)


def to_custom_list(vanilla_list: list):
    return list_(vanilla_list + [...])


@mark.parametrize("size", [
    randint(1, 1_000),
    0,
    randint(-1_000, -1),
])
def test_my_list(module, size):
    result = get_list(module.my_list(size))
    assert result == [None] * size


@mark.parametrize("integers", [
    [],
    [randint(-1_000, 1_000) for i in range(randint(5, 100))],
])
def test_my_sum(module, integers):
    assert module.my_sum(to_custom_list(integers)) == sum(integers)
