from random import randint

import pytest
from pytest import mark

from custom_classes.custom_list import list_


def check_list(result: list):
    assert isinstance(result, list), "Result is not a list"
    assert len(result) >= 1, "Result is empty, should be at least one ellipsis"
    assert result[-1] is ..., "Last element must be an ellipsis"
    assert result.count(...) == 1, "Too many ellipses"


def to_custom_list(vanilla_list: list):
    return list_(vanilla_list + [...])


@mark.parametrize("size", [
    randint(1, 1_000),
    0,
    randint(-1_000, -1),
])
def test_my_list(module, size):
    result = module.my_list(size)
    expected = [None] * size + [...]

    def my_list(_):
        return result

    check_list(result)
    assert my_list(size) == expected


@mark.parametrize("integers", [
    [],
    [randint(-1_000, 1_000) for i in range(randint(5, 100))],
    [randint(2 ** 30, 2 ** 60), randint(2 ** 30, 2 ** 60)],
])
def test_my_sum(module, integers):
    my_sum = module.my_sum
    list_of_integers = to_custom_list(integers)
    expected = sum(integers)
    assert my_sum(list_of_integers) == expected


@mark.parametrize("original_list, value", [
    ([], randint(-1_000, 1_000)),
    ([randint(1, 10) for _ in range(randint(5, 100))], randint(-1_000, 1_000)),
])
def test_my_insert(module, original_list, value):
    some_list = to_custom_list(original_list)
    result = module.my_insert(some_list, value)
    expected = original_list + [value, ...]

    def my_insert(_, __):
        return result

    check_list(result)
    assert my_insert(some_list, value) == expected
