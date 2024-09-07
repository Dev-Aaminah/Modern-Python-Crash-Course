# Python Looping and Input Techniques

This guide provides an overview of various looping structures and input methods in Python, emphasizing static type annotations.

## Table of Contents

- [Python Looping and Input Techniques](#python-looping-and-input-techniques)
  - [Table of Contents](#table-of-contents)
  - [1. While Loop](#1-while-loop)
    - [Example:](#example)
  - [2. For Loop](#2-for-loop)
    - [Example:](#example-1)
  - [3. Control Statements](#3-control-statements)
    - [Break](#break)
    - [Continue](#continue)
    - [Pass](#pass)
    - [4. Input Function](#4-input-function)
    - [5. Command Line Arguments (sys.argv)](#5-command-line-arguments-sysargv)
      - [1. Examples](#1-examples)

---

## 1. While Loop

The `while` loop runs as long as a condition is `True`.

### Example:

```python
i: int = 0
while i < 5:
    print(i)
    i += 1
```
Type hinting: i: int indicates that i is an integer.

## 2. For Loop
The for loop iterates over items of a collection (like a list, tuple, dictionary, etc.).

### Example:
```python
nums: list[int] = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
```
Type hinting: nums: list[int] specifies that nums is a list of integers.

## 3. Control Statements
Control statements alter the flow of a loop. The main control statements are break, continue, and pass.

### Break
Exits the loop prematurely.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Continue
Skips the current iteration and moves to the next one.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```


### Pass
Does nothing and is typically used as a placeholder.

```python
for i in range(5):
    pass  # No action taken, just a placeholder.
```

### 4. Input Function
Used to take user input from the console.

Example:
```python
name: str = input("Enter your name: ")
print(f"Hello, {name}!")
```

### 5. Command Line Arguments (sys.argv)
You can pass arguments to a Python script from the command line using the sys.argv list.

Example:
```python
import sys
args: list[str] = sys.argv

print(f"Script name: {args[0]}")
if len(args) > 1:
    print(f"First argument: {args[1]}")
```
sys.argv[0] is the script name, and subsequent elements are the command-line arguments.

#### 1. Examples
While Loop Example:
```python
n: int = 1
while n <= 10:
    print(n)
    n += 1
```

For Loop Example:
```python
fruits: list[str] = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Input Example:
```python
age: int = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```