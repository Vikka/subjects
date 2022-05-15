# Practice with str

## Summary

- [Exercise 1: string_length][exercise 1 header]
- [Exercise 2: reverse_string][exercise 2 header]
- [Exercise 3: is_uppercase][exercise 3 header]
- [Exercise 4: is_capitalize][exercise 4 header]
- [Exercise 5: my_count][exercise 5 header]
- [Exercise 6: my_split][exercise 6 header]

## Exercises

### [Exercise 1: string_length][summary header]

Create a function `string_length` that takes a string as argument and returns
the length of the string. You will use `'\0'` as a character that represents
the end of a string. It's a SINGLE character (eg. `len('\0') == 1`).

#### Exemple:

```shell
>>> string_length("Hello\0")
5
>>> string_length("\0")
0
>>> string_length("Lorem ipsum dolor sit amet\0")
26
```

#### Hints:

- [Python Tutorial for Beginners 2: Strings - Working with Textual Data][youtube strings]
- No, you can't use the `len()` function!
- Why `'\0'`? Because we will mimic the C NUL terminator.
  See [this StackOverflow answer][stackoverflow 1]
- No, you can't name the function `SarahConnor`, because it's not PEP8
  compliant.

### [Exercise 2: reverse_string][summary header]

Create a function `reverse_string` that takes a string as argument and returns
the string in reverse.

#### Exemple:

```shell
>>> reverse_string("Hello\0")
'olleH\0'
>>> reverse_string("\0")
'\0'
>>> reverse_string("H\0")
'H\0'
>>> reverse_string("Hello World\0")
'dlroW olleH\0'
```

#### Hints:

- Did you know that you can use negative indexes in a string indexing?
  e.g. "Hello"[-1] == "l"
- Of course, you can't use `reverse()`, don't even think about it.
- Did you notice that the `'\0'` is not reversed? It's because it should always
  be at the end of the string.

### [Exercise 3: is_uppercase][summary header]

Create a function `is_uppercase` that takes a string and returns `True` if the
string is in uppercase, `False` otherwise. If the string is empty, return
`False`.

#### Exemple:

```shell
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
```

#### Hints:

- Did you know the ascii table? No? Look at [What is ASCII?][youtube ascii]
- Do you know that you can use `ord()` to get the ascii value of a character
  and
  `chr()` to get the character from an integer?
  e.g. `ord('a') == 97`, `chr(97) == 'a'`

### [Exercise 4: is_capitalize][summary header]

Create a function `is_capitalize` that takes a string and returns `True` if
each words of the string is capitalized. If the string is empty (only contains
a `'\0'`, return `False`.

#### Exemple:

```shell
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
```

#### Hints:

- Good luck!

### [Exercise 5: my_count][summary header]

Create a function `my_count` that takes a string and a character as parameters
and return the number of occurrence of the character in the string. This is
case-insensitive (e.g. `"a"` and `"A"` is considered as the same character).

#### Exemple:

```shell
>>> my_count("HELLO\0", "H")
1
>>> my_count("HELLO\0", "l")
2
>>> my_count("HELLO\0", "z")
0
>>> my_count("\0", "z")
0
>>> my_count("Hello\0", "")
0
>>> my_count("aaAA\0", "a")
4
```

#### Hints:

- How to know if a character is the uppercase version of another character
  without `.upper()` or `.lower()`?

### [Exercise 6: my_split][summary header]

Create a function `my_split` that takes a string and returns the number of
words inside the string. A word is a sequence of characters separated by a
space. Special characters are considered as part of a word.

#### Exemple:

```shell
>>> my_split("Hello World\0") 
2
>>> my_split("Hello\0")
1
>>> my_split("\0")    
0
>>> my_split("Hello! World\0")
2
>>> my_split("Hello World !\0")
3
```

#### Hints:

- No idea how to help you for this one yet.

###### Copyright © 2022 Dorian Turba

[summary header]: #Summary

[exercise 1 header]: #exercise-1-stringlength

[youtube strings]: https://youtu.be/k9TUPpGqYTo

[stackoverflow 1]: https://stackoverflow.com/a/4711475/6251742

[exercise 2 header]: #exercise-2-reverse_string

[exercise 3 header]: #exercise-3-is_uppercase

[youtube ascii]: https://youtu.be/zB85kTs-sEw

[exercise 4 header]: #exercise-4-is_capitalize

[exercise 5 header]: #exercise-5-my_count

[exercise 6 header]: #exercise-6-my_split
