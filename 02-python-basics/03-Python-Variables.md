## **Variable in Python**

- Variables are **named references** to an object stored in the **heap memory**.
- Unlike other languages, variables does not store objects, variables/names are bind to objects.
- Objects owns the memory space not the variables.
- **Purpose** - Eliminate the need to handle memory addresses directly and code reusability.
- **Properties:** - Variables does not store values, they refer to it and Variables have dynamic type.

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

## **Parallel and Chained Assignment**

1. **Chained Assignment:** Involves assigning a single value to multiple variables.
`left_ptr = right_ptr = 0`
2. **Parallel Assignment (Tuple Unpacking):** Invloves assigning multiple values to multiple variables.
`left_ptr, right_ptr = 1, 0`

## **Iterable Unpacking**

1. Distributing values of an iterable to separate variables.
`_variable_1, _variable_2 = iterable`

```python
person = 'Jane doe', '20'
name, age = person
print(name) # 'Jane doe'
```
2. **Flexible Unpacking:** Use **\*** for flexible unpacking.
   
```python
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c) # 1, [2, 3, 4], 5
```
## Deleting Variable
- `del` keyword is used to delete the variable reference not the actual objects.
`del x`

## **Naming Rules for Variables**

1. Variables can be any length and can consist -Letters (`A-Z`)(`a-z`), digits (`0-9`), and the underscore (`_`).
2. Cannot start with digits.
3. Cannot use Python **keywords** (e.g., `if`, `True`, `def`).
4. Variables are case-sensitive.

## **Best Practices**

1. Variables should be descriptive.
2. **Variables/Functions:** `snake_case` (e.g., `calculate_area`) 'camelCase` (e.g., `calculateArea`).
3. **Classes:** `PascalCase` (e.g., `UserProfile`)
4. **Constants:** `UPPERCASE` (e.g., `PI`).
5. Plural names for iterables.
6. Use **single underscores** for private attributes or methods. (e.g., `_amount` = 1000)

## **Common Errors**

1. Using keywords as variables will throw `SyntaxError`.
2. Overwriting built-in functions or types (e.g., `list`, `str`, `print`) can lead to unintended behavior and can cause `TypeError`.
3. Undefined variables can cause `NameError`.
4. Conflicting local and global variables could cause `UnboundLocalError`.
5. Soft keywords are **context-dependent** keywords that act as keywords only in specific situations but can be used as variable names elsewhere. (eg., `match`)
6. Incorrect unpacking will lead to `ValueError`.
