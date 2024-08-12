# Python Basics

This guide briefly introduces some of the foundational concepts in the Python programming language, including:

- [Python Basics](#python-basics)
  - [Python Operators](#python-operators)
    - [Arithmetic Operators:](#arithmetic-operators)
    - [Comparison Operators:](#comparison-operators)
    - [Logical Operators:](#logical-operators)
  - [Python Assignment Operators](#python-assignment-operators)
  - [Comments](#comments)
    - [Single-line comment:](#single-line-comment)
- [This is a single-line comment](#this-is-a-single-line-comment)
- [The Zen of Python, by Tim Peters](#the-zen-of-python-by-tim-peters)

## Python Operators

Python supports a variety of operators, which can be categorized as:

### Arithmetic Operators:
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division
- `%` : Modulus
- `**` : Exponentiation
- `//` : Floor division

### Comparison Operators:
- `==` : Equal to
- `!=` : Not equal to
- `>`  : Greater than
- `<`  : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

### Logical Operators:
- `and` : Logical AND
- `or`  : Logical OR
- `not` : Logical NOT
- `:=`  : Assignment expression (also known as the "walrus operator")

... and many more.

For a comprehensive list, refer to the official Python documentation.

## Python Assignment Operators

Python assignment operators are used to assign values to variables. These operators include simple assignment, as well as operators that perform an operation and then assign the result to the variable. Here is a table of some common assignment operators in Python:

| No. | Operator | Example   | Same As       |
|-----|----------|-----------|---------------|
| 0   | =        | x = 5     | x = 5         |
| 1   | +=       | x += 3    | x = x + 3     |
| 2   | -=       | x -= 3    | x = x - 3     |
| 3   | *=       | x *= 3    | x = x * 3     |
| 4   | /=       | x /= 3    | x = x / 3     |
| 5   | %=       | x %= 3    | x = x % 3     |
| 6   | //=      | x //= 3   | x = x // 3    |
| 7   | **=      | x **= 3   | x = x ** 3    |
| 8   | &=       | x &= 3    | x = x & 3     |
| 9   | \|=      | x \|= 3   | x = x \| 3    |
| 10  | ^=       | x ^= 3    | x = x ^ 3     |
| 11  | >>=      | x >>= 3   | x = x >> 3    |
| 12  | <<=      | x <<= 3   | x = x << 3    |

These assignment operators are commonly used in various programming tasks, and understanding them is fundamental to writing efficient Python code.

## Comments

In Python, comments are lines that are not executed by the interpreter. They're used to explain code and improve readability.

### Single-line comment:
Starts with `#`

```python
# This is a single-line comment
print("Hello, World!")  # This is an inline comment


# The Zen of Python, by Tim Peters

> Beautiful is better than ugly.  
> Explicit is better than implicit.  
> Simple is better than complex.  
> Complex is better than complicated.  
> Flat is better than nested.  
> Sparse is better than dense.  
> Readability counts.  
> Special cases aren't special enough to break the rules.  
> Although practicality beats purity.  
> Errors should never pass silently.  
> Unless explicitly silenced.  
> In the face of ambiguity, refuse the temptation to guess.  
> There should be one-- and preferably only one --obvious way to do it.  
> Although that way may not be obvious at first unless you're Dutch.  
> Now is better than never.  
> Although never is often better than *right* now.  
> If the implementation is hard to explain, it's a bad idea.  
> If the implementation is easy to explain, it may be a good idea.  
> Namespaces are one honking great idea -- let's do more of those!