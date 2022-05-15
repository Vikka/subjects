# Practice with lists

## Summary

- [Exercise 1: my_list][exercise 1 header]
- [Exercise 2: my_sum][exercise 2 header]
- [Exercise 3: my_insert][exercise 3 header]
- [Exercise 4: my_concat][exercise 4 header]

## Exercises

### [Exercise 1: my_list][summary header]

Create a function "my_list" that takes one integer as size and returns a list
of that size filled with `None` values plus one element with the value `...`
(an **ellipsis**) that will be considered as the end of the list. Negative
values will be considered as `0`.

#### Exemple:

```shell
>>> my_list(5)
[None, None, None, None, None, ellipsis]
>>> my_list(-1)
[ellipsis]
```

#### Hints:

- You can use the `*` operator (eg. `[None] * 3` will
  create `[None, None, None]`).
- If you can append a value at the end of a list, maybe you should create a
  bigger one at first and change the value of the last element?
- Be careful with the `...` value. It's not `"..."` or `'...'`. Those values
  are **strings**, not an **ellipsis** (yes, `...` is what we call an
  ellipsis). Also, don't be afraid if python print the `...` as `ellipsis`
  (eg. `print(...)` display 'ellipsis').

### [Exercise 2: my_sum][summary header]

Create a function `my_sum` that takes a list of integers as argument and
returns the sum of all the elements of the list. The list always contains an
`ellipsis` at its last index. If the list contains no integers, return `0`.

#### Exemple:

```shell
>>> my_sum([1, 2, 3, ...])
6
>>> my_sum([...])
0
```

#### Hint:

- While is your friend: https://youtu.be/jSs58VZVLw8
- Remember, you aren't allowed to use break statements.
- `1 != ...` is `True` while `1 == ...` is `False`.

### [Exercise 3: my_insert][summary header]

Create a function "my_insert" that takes a list and a value as arguments and
returns a new list that is the concatenation of the two lists. Be careful, the
type of the inserted value must be the same as the type of the elements of the
list. If it's not, you must return the orginal list unchanged.

#### Exemple:

```shell
>>> my_insert([1, 2, 3, ...], 4)
[1, 2, 3, 4, ellipsis]
>>> my_insert([1, 2, 3, ...], "4")
[1, 2, 3, ellipsis]
>>> my_insert(["1", "2", "3", ...], 4)
["1", "2", "3", ellipsis]
```

#### Hints:

- `my_list` function will be useful :D
- Also, remember how you added the `ellipsis` at the end of the list
  in `my_list`.

### [Exercise 4: my_concat][summary header]

Create a function `my_concat` that takes two lists as arguments and returns a
new list that is the concatenation of the two lists. Be careful, the type of
the second list must be the same as types of elements of the list first. If
it's not, you must return the first list unchanged.

#### Exemple:

```shell
>>> my_concat([1, 2, 3, ...], [4, 5, 6, ...])
[1, 2, 3, 4, 5, 6, ellipsis]
>>> my_concat([1, 2, 3, ...], ["4", "5", "6", ...])
[1, 2, 3, ellipsis]
>>> my_concat(["1", "2", "3", ...], [4, 5, 6, ...])
["1", "2", "3", ellipsis]
>>> my_concat([1, 2, 3, ...], [4, 5, "6", ...])
[1, 2, 3, ellipsis]
>>> my_concat([1, 2.0, "a", ...], [4, 5.0, "b", ...])
[1, 2.0, "a", 4, 5.0, "b", ellipsis]
```

#### Hints:

- If you can't increase the size of a list with `.append()`, maybe you should
  create a bigger one and replace its content instead?

###### Copyright © 2022 Dorian Turba

[summary header]: #Summary

[exercise 1 header]: #exercise-1-my_list

[exercise 2 header]: #exercise-2-my_sum

[exercise 3 header]: #exercise-3-my_insert

[exercise 4 header]: #exercise-4-my_concat