# Python Control Flow and Typing Guide

This guide provides an overview of Python's control flow structures, including `if`, `if-else`, `if-elif-else`, and nested `if-else-elif` statements. Additionally, it covers the use of Python's static type annotations, the `Union` and `Optional` types from the `typing` module, the `zip` function with lists, and sorting a list of tuples based on the second tuple index.

## Table of Contents
- [Python Control Flow and Typing Guide](#python-control-flow-and-typing-guide)
  - [Table of Contents](#table-of-contents)
  - [If Statement](#if-statement)
  - [If-Else Statement](#if-else-statement)
  - [Nested If-Else-Elif](#nested-if-else-elif)

## If Statement
```python
x: int = 10
if x > 5:
    print("x is greater than 5")


## If-Else Statement

The `if-else` statement allows you to execute one block of code if a condition is true, and another block if it is false.

```python
x: int = 4
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


## Nested If-Else-Elif
x: int = 10
y: int = 5
if x > 5:
    if y > 5:
        print("x and y are both greater than 5")
    else:
        print("x is greater than 5 but y is not")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

