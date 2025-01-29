## **Variable in Python**

- Variables are named references to an object stored in the heap memory.
- **Purpose** - Eliminate the need to handle memory addresses directly and code reusability.

## **Dynamically Typed**

- Variables are not explicitly declared with a data type.
- It is inferred from the object.
- The type of the variable is checked at runtime and can be changed.
- `_variable = 10 # inferred as integer object.`

## **Identifier in Python**

- An **identifier** is a name used to define variables, functions, classes, and other Python objects.
- Identifiers are case-sensitive.
- Variables are instances of an identifier that point to a value.

## **Variables Assignment**

- To create a variable, **assign** it a value using the assignment operator.
- The value in this construct can be any Python object.
- **Standard Assignment:**  `name = "Alice"`

## **Parallel or Chained Assignment**

- Allows multiple assignments in a single line.
- Involves assigning a single value to multiple variables.
- `left_ptr, right_ptr = 0`

## **Iterable Unpacking**

- Distributing values of an iterable to separate variables.
- `_variable_1, _variable_2 = iterable`

```python
In [17]: person = 'Jane doe', '20'
In [18]: name, age = person
In [19]: name
Out[19]: 'Jane doe'
```

## **Naming Rules for Variables**

1. Variables can be any length and can consist of uppercase letters (`A-Z`) and lowercase letters (`a-z`), digits (`0-9`), and the underscore (`_`).
2. Cannot start with digits.
3. No special characters. `π = 3.14`
4. Cannot use Python **keywords** (e.g., `if`, `True`, `def`).

## **Best Practices**

- Variables/Functions: `snake_case` (e.g., `calculate_area`)
- Classes: `PascalCase` (e.g., `UserProfile`)
- Constants: `UPPERCASE` (e.g., `PI`).
- Plural names for iterables.
- Use **single underscores** for private attributes or methods.

## **Common Errors**

- Using keywords as variables will throw `SyntaxError`.
- Overwriting built-in functions or types (e.g., `list`, `str`, `print`) can lead to unintended behavior and can cause `TypeError`.
- Undefined variables can cause `NameError`.
- Conflicting local and global variables could cause `UnboundLocalError`.
- Soft keywords are **context-dependent** keywords that act as keywords only in specific situations but can be used as variable names elsewhere.