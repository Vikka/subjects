# Practice with problems

## Summary

- [Exercise 1: my_fizzbuzz][exercise 1 header]
- [Exercise 2: my_strange_multiply][exercise 2 header]
- [Exercise 3: product_on_list][exercise 3 header]

## Exercises

### [Exercise 1: my_fizzbuzz][summary header]

!Disclaimer: all lists and strings must finish with `...` and `'\0'`,
respectively.
It's just not displayed in the subject for convinience.

Create a function "my_fizzbuzz" that:

- takes a list of int as argument

1. replace in the list each multiple of 3 by "Fizz", each multiple of 5 by
   "Buzz", and each multiple of 3 and 5 by "FizzBuzz":

```
[1, 3, 5, 15]
 => [1, 'fizz', 'buzz', 'fizzbuzz']
```

2. replace each value of the list with itself converted to string:

```
[1, 'fizz', 'buzz', 'fizzbuzz']
 => ['1', 'fizz', 'buzz', 'fizzbuzz']
```

3. replace each value with a list of each character of the string,

```
['1', 'fizz', 'buzz', 'fizzbuzz']
 => [['1'], ['f', 'i', 'z', 'z'], ['b', 'u', 'z', 'z'], ['f', 'i', 'z', 'z', 'b', 'u', 'z', 'z']]
```

4. replace each character in each list of string by its ascii value:

```
[['1'], ['f', 'i', 'z', 'z'], ['b', 'u', 'z', 'z'], ['f', 'i', 'z', 'z', 'b', 'u', 'z', 'z']]
 => [[49], [102, 105, 122, 122], [98, 117, 122, 122], [102, 105, 122, 122, 98, 117, 122, 122]]
```

5. replace each list of characters by it's sum:

```
[[49], [102, 105, 122, 122], [98, 117, 122, 122], [102, 105, 122, 122, 98, 117, 122, 122]]
 => [49, 451, 459, 910]
```

6. get the product of the value of the list:

```
[49, 451, 459, 910]
 => 9230531310
```

7. convert this value to a string and create a list of ascii values of each
   character:

```
9230531310
 => [57, 50, 51, 48, 53, 51, 49, 51, 49, 48]
```

8. return the sum of this list:

```
[57, 50, 51, 48, 53, 51, 49, 51, 49, 48]
 => 507
```

#### Exemple:

```
>>> my_fizzbuzz([1, 2, 3, 4, 5, 6, 7, 8, 9, ...])
1032
>>> my_fizzbuzz([1,50, 150, 300, 500, 1000, ...])
840
```

#### Hints:

- Remember, you can create functions and use them as many times as you want.
- Proceed step by step.

### [Exercise 2: my_strange_multiply][summary header]

!Disclaimer: all lists and strings must finish with `...` and `'\0'`,
respectively.
It's just not displayed in the subject for convinience.

Create a function "my_strange_multiply" that:

- takes a list of int as argument

1. replace in the list each number such that the new value is the product of
   all the numbers in the original list except the one at that is replaced:

```
[1, 2, 3, 4, 5]
 => [120, 60, 40, 30, 24]
```

2. convert each value of the list to string:

```
[120, 60, 40, 30, 24]
 => ['120', '60', '40', '30', '24']
```

3. concatenate each value of the list:

```
['120', '60', '40', '30', '24']
 => '12060403024'
```

4. convert the string in a list where each character is an element of the
   list converted to an integer:

```
'12060403024'
 => [1, 2, 0, 6, 0, 4, 0, 3, 0, 2, 4]
```

5. replace each value with the n square 'th value of the fibonacci sequence
   where n is the original value:

```
[1, 2, 0, 6, 0, 4, 0, 3, 0, 2, 4]
 => [1, 3, 0, 14930352, 0, 987, 0, 34, 0, 3, 987]
```

6. Subtract each value of the list except the largest number to the largest
   number:

```
[1, 3, 0, 14930352, 0, 987, 0, 34, 0, 3, 987]
 => 14928337
```

#### Exemple:

```
>>> my_strange_multiply([1, 2, 3, 4, 5, ...])
14928337
>>> my_strange_multiply([...])
0
```

#### Hints:

    - https://en.wikipedia.org/wiki/Fibonacci_number


### [Exercise 3: product_on_list][summary header]

Create a function that take a list of int and return a new array

#### Exemple:

```
>>> product_on_list([1, 2, 3, 4, 5, ...])
[120, 60, 40, 30, 24, ...]
>>> product_on_list([...])
0
```

Copyright © 2022 Dorian Turba

[summary header]: #Summary

[exercise 1 header]: #exercise-1-my_list

[exercise 2 header]: #exercise-2-my_strange_multiply

[exercise 3 header]: #exercise-3-product_on_list
