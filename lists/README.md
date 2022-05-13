# lists

exercise 1:

```txt
Create a function "my_list" that takes one integer as size and returns a list of that size
filled with None values plus one element with the value "..." (an ellipsis) that will be
considered as the end of the list. Negative values will be considered as 0.

    Exemple:
        >>> my_list(5)
        [None, None, None, None, None, ellipsis]
        >>> my_list(-1)
        [ellipsis]

    Hint:
        - You can use the "*" operator (eg. [None] * 3 will create [None, None, None]).
        - If you can append a value at the end of a list, maybe you should create a bigger one at
        first and change the value of the last element?
        - Be careful with the ... value. It's not "..." or '...'. Those values are strings, not an
        ellipsis (yes, ... is what we call an ellipsis). Also, don't be afraid if python print the
        ... as "ellipsis" (eg. print(...) display 'ellipsis').
```

exercise 2:
```txt
Create a function "my_sum" that takes a list of integers as argument and returns the sum of
    all the elements of the list. If the list is empty, return 0.

    Exemple:
        >>> my_sum([1, 2, 3, ...])
        6
        >>> my_sum([...])
        0

    Hint:
        - While is your friend: https://youtu.be/jSs58VZVLw8
        - Remember, you aren't allowed to use break statements.
```
exercise 3:
```txt
Create a function "my_insert" that takes a list and a value as arguments and returns a new list
    that is the concatenation of the two lists. Be careful, the type of the inserted value must be
    the same as the type of the elements of the list. If it's not, you must return the orginal list
    unchanged.

    Exemple:
        >>> my_insert([1, 2, 3, ...], 4)
        [1, 2, 3, 4, ellipsis]
        >>> my_insert([1, 2, 3, ...], "4")
        [1, 2, 3, ellipsis]
        >>> my_insert(["1", "2", "3", ...], 4)
        ["1", "2", "3", ellipsis]

    Hints:
        - my_list will be useful :D
        - Also, remember how you added the ellipsis at the end of the list in my_list.
```
exercise 4:
```txt
Create a function "my_concat" that takes two lists as arguments and returns a new list
    that is the concatenation of the two lists. Be careful, the type of the inserted value must be
    the same as the type of the elements of the list. If it's not, you must return the original list
    unchanged.

    Exemple:
        >>> my_concat([1, 2, 3, ...], [4, 5, 6, ...])
        [1, 2, 3, 4, 5, 6, ellipsis]
        >>> my_concat([1, 2, 3, ...], ["4", "5", "6", ...])
        [1, 2, 3, ellipsis]
        >>> my_concat(["1", "2", "3", ...], [4, 5, 6, ...])
        ["1", "2", "3", ellipsis]

    Hints:
        - If you can't increase the size of a list, maybe you should create a bigger one and
        do stuff with it?
```

###### Copyright © 2022 Dorian Turba
