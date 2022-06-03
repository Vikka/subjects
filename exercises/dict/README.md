# Practice with functions

## Summary

- [Exercise 1: my_add][exercise 1 header]

## Exercises

### [Exercise 1: my_keys][summary header]

Create a function "my_keys" that takes a dictionary as an argument and returns
a list of keys with an ellipsis at the end of the list.

#### Exemple:

```
>>> my_keys({'a': 1, 'b': 2})
['a', 'b', ...]
```

#### Hints:

- If you cast a dictionary to a list, the list will contain the keys.
- https://youtu.be/daefaLgNkw0

### [Exercise 2: my_values][summary header]

Create a function "my_values" that takes a dictionary as an argument and
returns the list of values with an ellipsis at the end of the list. The order
of the values doesn't matter.

#### Exemple:

```
>>> my_values({'a': 1, 'b': 2})
[1, 2, ...]
```

### [Exercise 3: my_items][summary header]

Create a function "my_items" that takes a dictionary as an argument and
returns a list of tuples with two values inside. The first value is the key
and the second value is the value. The list must end with an ellipsis. The
order of the tuples doesn't matter.

#### Exemple:

```
>>> my_items({'a': 1, 'b': 2})
[('a', 1), ('b', 2), ...]
```

### [Exercise 4: my_update][summary header]

Create a function "my_update" that takes two dictionaries as arguments and
replace the values of the first dictionary with the values of the second
dictionary.

#### Exemple:

```
>>> a = {'a': 1, 'b': 2}
>>> b = {'b': 3, 'c': 4}
>>> my_update(a, b)
>>> a
{'a': 1, 'b': 3, 'c': 4}
```

### [Exercise 5: my_merge][summary header]

Create a function "my_merge" that takes two dictionaries as arguments and
returns a new dictionary with the values of the first dictionary updated with
the values of the second dictionary. If the same key is present in both
dictionaries, the value of the second dictionary will be used.

#### Exemple:

```
>>> my_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
{'a': 1, 'b': 3, 'c': 4}
```

### [Exercise 6: my_filter][summary header]

Create a function "my_filter" that takes a dictionary and a function as
arguments. The function must return a list of keys of values accepted by the
function ended by an ellipsis.

#### Exemple:

```
>>> def filter_even(x):
...     return x % 2 == 0
...
>>> my_filter({'a': 1, 'b': 2}, lambda x: x > 1)
['b', ...]
```

### [Exercise 7: my_del][summary header]

Create a function "my_del" that takes a dictionary and a list of keys as
arguments. The function must delete the keys from the dictionary.

#### Exemple:

```
>>> my_del({'a': 1, 'b': 2}, ['a', ...])
>>> {'b': 2}
>>> my_del({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', ...])
>>> {'c': 3}
>>> my_del({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'c', ...])
>>> {}
```

### [Exercise 8: my_value_getter][summary header]

Create a function "my_value_getter" that takes a dictionary, a value used as
key, and a third value used a default value. The function must return the value
of the key. If the key is not present in the dictionary, the default value must
be returned.

#### Exemple:

```
>>> my_value_getter({'a': 1, 'b': 2}, 'a', 0)
1
>>> my_value_getter({'a': 1, 'b': 2}, 'c', 0)
0
```

Copyright © 2022 Dorian Turba

[summary header]: #Summary

[exercise 1 header]: #exercise-1-my_add

[youtube 1]: https://youtu.be/u-OmVr_fT4s

[exercise 2 header]: #exercise-2-my_sum