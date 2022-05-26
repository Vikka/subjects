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


@mark.parametrize("string, expected", [
    ("Hello", "olleH"),
    ("", ""),
    ("Lorem ipsum dolor sit amet", "tema tis rolod muspi meroL"),
])
def test_reverse_string(module, string, expected):
    string = to_custom_str(string)
    expected = to_custom_str(expected)
    result = module.reverse_string(string)

    def reverse_string(_):
        return result

    check_str(result)
    assert reverse_string(string) == expected


@mark.parametrize("string", [
    (''.join(sample(ascii_letters, randint(10, 50)))),
    (''.join([choice(ascii_lowercase) for _ in range(randint(1000, 2000))])),
])
def test_reverse_string_rand(module, string):
    expected = to_custom_str(string[::-1])
    string = to_custom_str(string)
    result = module.reverse_string(string)

    def reverse_string(_):
        return result

    check_str(result)
    assert reverse_string(string) == expected


@mark.parametrize("string, expected", [
    ("hello", False),
    ("hello world", False),
    ("Hello", False),
    ("AAAA", True),
    ("ZZZZ", True),
    ("", False),
    ("HELLO", True),
    ("HELLO WORLD", True),
    ("HELLO !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~WORLD", True),
    ("HELLO !\"#$%&'()*+,-./:i;<=>?@[\\]^_`{|}~WORLD", False),
])
def test_is_uppercase(module, string, expected):
    string = to_custom_str(string)
    result = module.is_uppercase(string)

    def is_uppercase(_):
        return result

    assert is_uppercase(string) == expected


@mark.parametrize("string, expected", [
    ("Hello", True),
    ("HELLO", False),
    ("HellO", False),
    ("", False),
    ("Lorem ipsum dolor sit amet", False),
    ("Lorem Ipsum Dolor Sit Amet", True),
    ("HELLO", False),
    ("HELLO WORLD", False),
    ("HELLO !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~WORLD", False),
    ("Hello !\"#$%&'()*+,-./:I;<=>?@[\\]^_`{|}~World", True),
])
def test_is_capitalized(module, string, expected):
    string = to_custom_str(string)
    result = module.is_capitalized(string)

    def is_capitalized(_):
        return result

    assert is_capitalized(string) == expected

# my_count
@mark.parametrize("string, letter, expected", [
    ("Hello", 'H', 1),
    ("Hello", 'l', 2),
    ("Hello", 'z', 0),
    ('', 'z', 0),
    ('Hello', '', 0),
    ('aaAA', 'a', 4),
    ('aaAA', 'A', 4),
])
def test_my_count(module, string, letter, expected):
    string = to_custom_str(string)
    letter = to_custom_str(letter)
    result = module.my_count(string, letter)

    def my_count(_):
        return result

    assert my_count(string) == expected
