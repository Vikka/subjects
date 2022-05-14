# Logic training with Python

## Setup

Install requirements:

```
pip install -r requirements.txt
```

## How to run test suite

### On a specific folder

This is an example, and a good start.

```
python -m pytest exercises/function
```

### On all folders

Note: You will get a lot of errors if not all required functions are
implemented.

```
python -m pytest
```

# Rules

## Forbidden python features

- imports,
- from imports,
- defining functions with builtin names,
- calls of function with builtin names
  except ['int', 'list', 'dict', 'bool', 'str', 'float', 'tuple', 'None', 'type']
  ,
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
- 3 args form of type,
- class definitions,
- in and not in operator,
- is and is not operator,
- positional only arguments, keyword only arguments, keywords defaults
  arguments, defaults arguments, variadic arguments, variadic keyword
  arguments,
- slices,

# Useful links

- [pythontutor, understand python memory](https://pythontutor.com/)
- [Codingame](https://www.codingame.com/home)

###### Copyright © 2022 Dorian Turba
