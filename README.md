# Logic training with Python

Usage of Internet is authorized.

## Setup

[Install requirements][SA-install requirements.txt with pip]
(with [pip][pip tutorial on youtube]):

```shell
pip install -r requirements.txt
```

## How to run test suite

### Code in fill_me.py files

If you want to test your code, put your functions inside fill_me.py files.

### On a specific folder

This is an example, and a good start.

```shell
pytest exercises/function
# or
python -m pytest exercises/function
```

### On all folders

Note: You will get a lot of errors if not all required functions are
implemented.

```shell
pytest
# or
python -m pytest
```

# Rules

## Forbidden python features

- imports,
- from imports,
- defining functions with builtin names,
- calls of function with builtin names
  except ['int', 'list', 'dict', 'bool', 'str', 'float', 'tuple', 'type',
'ord', 'chr'],
- calls of methods (eg. 'my_list.append()'),
- try clauses,
- break and continue statements,
- variables with builtin names or trailing underscore (eg. 'my_var_'),
- for loop,
- list comprehensions,
- dict comprehensions,
- set comprehensions,
- generator expressions,
- yield and yield from statements,
- raise statements,
- assert statements,
- while else statements,
- global statements,
- nonlocal statements,
- following operators on
  list: ['+', '+=', '==', '>=', '<=', '>', '<', '!=', '*='],
- following operators on
  dict: ['+', '+=', '==', '>=', '<=', '>', '<', '!=', '*=', '|', '&'],
- 3 args form of type,
- class definitions,
- in and not in operator,
- is and is not operator,
- positional only arguments, keyword only arguments, keywords defaults
  arguments, defaults arguments, variadic arguments, variadic keyword
  arguments,
- slices,
- packing and unpacking,

## Respect PEP 8 style

PEP 8 is a style guide for Python. You can find it [here][PEP 8 page].

You must respect two other rules:

- Line length must be less than 80 characters,
- Function length must be less than 25 lines.

Since you aren't allowed to use some python features, you should test your
code with custom rules. This project has a `setup.cfg` file with
a [flake8][flake8 page] configuration, so you can run `flake8` to check your
code with properly excluded errors.

```shell
flake8
# or
python -m flake8
```

### What to do if an error is found

- If the error is raised by flake8 because you didn't use a forbidden feature,
  you should report it on the [issue tracker][issue tracker].
- If the error raised by flake8 is about complexity, you should reduce
  the [cognitive complexity][cognitive complexity PDF] of your code.

# Useful links

- [pythontutor, visualize python memory][pythontutor main page]
- [Codingame.com][codingame main page]

Copyright © 2022 Dorian Turba

[SA-install requirements.txt with pip]: https://stackoverflow.com/a/15593865/6251742

[pip tutorial on youtube]: https://youtu.be/U2ZN104hIcc

[pythontutor main page]: https://pythontutor.com/

[codingame main page]: https://www.codingame.com/home

[PEP 8 page]: https://www.python.org/dev/peps/pep-0008/

[flake8 page]: https://flake8.pycqa.org/en/latest/

[issue tracker]: https://github.com/Vikka/subjects/issues/new/choose

[cognitive complexity PDF]: https://www.sonarsource.com/docs/CognitiveComplexity.pdf
