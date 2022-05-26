from random import randint, choice, sample
from string import ascii_letters, ascii_lowercase

from pytest import mark


def check_str(result: str):
    assert isinstance(result, str), "Result is not a str"
    assert len(result) >= 1, "Result is empty, should be at least one '\\0'"
    assert result[-1] == '\0', "Last element must be an '\\0'"
    assert result.count('\0') == 1, "Too many '\\0'"


def to_custom_str(vanilla_str: str):
    return vanilla_str + '\0'


@mark.parametrize("string, expected", [
    ("Hello", 5),
    ("", 0),
    ("Lorem ipsum dolor sit amet", 26),
])
def test_string_length(module, string, expected):
    string = to_custom_str(string)
    result = module.string_length(string)

    def string_length(_):
        return result

    assert string_length(string) == expected


@mark.parametrize("string", [
    (''.join(sample(ascii_letters, randint(10, 50)))),
    (''.join([choice(ascii_lowercase) for _ in range(randint(1000, 2000))])),
])
def test_string_length_rand(module, string):
    expected = len(string)
    string = to_custom_str(string)
    result = module.string_length(string)

    def string_length(_):
        return result

    assert string_length(string) == expected
