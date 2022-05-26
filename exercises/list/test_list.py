from random import randint, choice, random, sample
from string import ascii_letters, ascii_lowercase

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
    ([choice(ascii_letters) for _ in range(randint(5, 100))],
     choice(ascii_letters)),
    ([randint(-5, 5)] * 2, choice(ascii_letters)),
])
def test_my_insert(module, original_list, value):
    some_list = to_custom_list(original_list)
    result = module.my_insert(some_list, value)
    expected = original_list + [value, ...] \
        if len(some_list) <= 1 or isinstance(value, type(some_list[0])) \
        else original_list + [...]

    def my_insert(_, __):
        return list(result)

    check_list(result)
    assert my_insert(some_list, value) == expected


@mark.parametrize("first_list, second_list, expected", [
    ([], [], [...]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6, ...]),
    ([1, 2, 3], ["4", "5", "6",], [1, 2, 3, ...]),
    (["1", "2", "3"], [4, 5, 6], ["1", "2", "3", ...]),
    ([1, 2.0, "a"], [4, 5.0, "b"], [1, 2.0, "a", 4, 5.0, "b", ...]),
])
def test_my_concat(module, first_list, second_list, expected):
    first_list = to_custom_list(first_list)
    second_list = to_custom_list(second_list)
    result = module.my_concat(first_list, second_list)

    def my_concat(_, __):
        return list(result)

    check_list(result)
    assert my_concat(first_list, second_list) == expected


@mark.parametrize("first_list, second_list", [
    (list(range(1_000)), list(range(1_000, 2_000))),
    ([randint(-5, 5), random(), choice(ascii_letters)],
     [randint(-5, 5), random(), choice(ascii_letters)]),
    (sample(list(range(10)) + list(ascii_lowercase), randint(5, 20)), [1, 3]),
])
def test_my_concat_rand(module, first_list, second_list):
    full_list = first_list + second_list
    types = {type(e) for e in first_list}
    is_same_type = all(type(e) in types for e in second_list)
    expected = full_list + [...] \
        if full_list and is_same_type \
        else first_list + [...]

    first_list = to_custom_list(first_list)
    second_list = to_custom_list(second_list)
    result = module.my_concat(first_list, second_list)

    def my_concat(_, __):
        return list(result)

    check_list(result)
    assert my_concat(first_list, second_list) == expected

