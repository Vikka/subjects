# str

Exercice 1:
```txt
Create a function string_length() that takes a string as argument and returns the length of the
    string. '\0' is a character that represents the end of a string. It's a SINGLE character.

    Exemple:
        >>> string_length("Hello\0")
        5
        >>> string_length("\0")
        0
        >>> string_length("Lorem ipsum dolor sit amet\0")
        26

    Hint:
        - https://youtu.be/k9TUPpGqYTo
        - No, you can't use the len() function!
        - Why \0? Because we will mimic the C NUL terminator.
        See https://stackoverflow.com/a/4711475/6251742
        - No, you can name the function "SarahConnor".
```
Exercice 2:
```txt
Create a function reverse_string() that takes a string as argument and returns the string in
    reverse.

    Exemple:
        >>> reverse_string("Hello\0")
        'olleH\0'
        >>> reverse_string("\0")
        '\0'
        >>> reverse_string("H")
        'H\0'
        >>> reverse_string("Hello World")
        'dlroW olleH\0'

    Hint:
        - Did you know that you can use negative indexes in a string indexing?
        eg. "Hello"[-1] == "l"
        - Of course, you can't use reverse(), don't even think about it.
        - Did you noticed that the '\0' is not reversed? It's because it should always be at the
        end of the string.
```

Exercice 3:
```txt
Create a function is_uppercase() that takes a string and returns True if the string is in
    uppercase. If the string is empty, return False.

    Exemple:
        >>> is_uppercase("HELLO\0")
        True
        >>> is_uppercase("HELLO WORLD\0")
        True
        >>> is_uppercase("hello world\0")
        False
        >>> is_uppercase("\0")
        False
        >>> is_uppercase("hELLO WORLD\0")
        False

    Hint:
        - Did you know the ascii table? No? Look at https://youtu.be/zB85kTs-sEw
        - Do you know that you can use ord() to get the ascii value of a character and
        chr() to get the character from an integer? Example: ord('a') => 97, chr(97) => 'a'
```
Exercice 4:
```txt
Create a function is_capitalize() that takes a string and returns True if each words of the
    string is capitalized. If the string is empty, return False.

    Exemple:
        >>> is_capitalize("HELLO\0")
        False
        >>> is_capitalize("Hello\0")
        True
        >>> is_capitalize("Hello World\0")
        True
        >>> is_capitalize("Hello world\0")
        False
        >>> is_capitalize("\0")
        False

    Hint:
        - Good luck!
```