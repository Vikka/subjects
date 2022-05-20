# Practice with problems

## Summary

- [Exercise 1: my_fizzbuzz][exercise 1 header]

## Exercises

### [Exercise 1: my_fizzbuzz][summary header]

!Disclaimer: all lists and strings must finish with `...` and `'\0'`, respectively.
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
  7. convert this value to a string and create a list of ascii values of each character:
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

Copyright © 2022 Dorian Turba

[summary header]: #Summary

[exercise 1 header]: #exercise-1-my_list
