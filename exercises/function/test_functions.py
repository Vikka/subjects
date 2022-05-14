from random import randint

from pytest import mark


@mark.parametrize("x, y", [
    (randint(1, 1_000_000), randint(1, 1_000_000)),
    (randint(-1_000_000, -1), randint(-1_000_000, -1)),
    (randint(-1_000_000, -1), randint(1, 1_000_000)),
])
def test_my_add(module, x, y):
    """
    Test function for my_add
    """
    assert module.my_add(x, y) == x + y


@mark.parametrize("a, b, c, d", [
    (randint(1, 1_000_000), randint(1, 1_000_000), randint(1, 1_000_000),
     randint(1, 1_000_000)),
    (randint(-1_000_000, -1), randint(-1_000_000, -1), randint(-1_000_000, -1),
     randint(-1_000_000, -1)),
    (randint(-1_000_000, -1), randint(1, 1_000_000), randint(-1_000_000, -1),
     randint(1, 1_000_000)),
])
def test_my_sum(module, a, b, c, d):
    """
    Test function for my_sum
    """
    assert module.my_sum(a, b, c, d) == a + b + c + d
