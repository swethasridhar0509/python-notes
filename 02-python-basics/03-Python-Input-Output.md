## Input / Output

- Programs need to communicate with the users, whether to get data or to provide results of the program.
- Built-in function `input()` - Allows to capture user input from the keyword.
- Built-in function `print()` - Allows to display results in the console.

## Reading Input

- The `input()`  is used to obtain data from the users.
- It passes the execution of the program and allows the user to type.
- Once the Enter key is pressed, the input is collected as a string, excluding the new line character.
- Any text (optional) added between the `()`  is passed to the optional **prompt** argument and will be displayed as a prompt.

```python
In [1]: name = input("Enter your name: ")
Enter your name: A

In [2]: name
Out[2]: 'A'
```

### Type Casting the input

- The input() reads and returns the user’s input as a string.
- If numbers are entered, it will be treated as a string.
- To handle this, covert the input to the appropriate type.

```python
In [3]: number = input("Enter a random number: ")
Enter a random number: 100

In [4]: number + 50
---------------------------------------------
TypeError: can only concatenate str (not "int") to str

In [5]: number = int(input("Enter a random number: "))
Enter a random number: 100

In [6]: number + 50
Out[6]: 150

In [7]: amount = float(input("Enter total amount: "))
Enter total amount: 50.90

In [8]: amount
Out[8]: 50.9
In [9]: type(amount)
Out[9]: float
In [10]: type(number)
Out[10]: int
```

## Display Results

- `print()`  displays the result to the console.
- Objects to be displayed are passed to the `print()` as comma separated list of arguments.
- By default, the objects are the separated by a single space and a newline is added at the end in the output.

```python
In [11]: fname = "John"
In [12]: lname = "Doe"

In [13]: print("full name:", fname, lname)
full name: John Doe
```

- The `print()` returns the string representation of the objects passed.

```python
In [14]: nums = [1, 2, 3]
In [15]: digit = 10
In [16]: _dict = {"yes" : 1, "no" : 0}

In [17]: print(nums, digit, _dict, len)
[1, 2, 3] 10 {'yes': 1, 'no': 0} <built-in function len>
```

- Additional keyword arguments of the print() can be used to format the output to some extent.
- **`sep`:** This argument allows you to specify how to separate multiple objects when they are printed.
- **`end`:** Use this argument to set what Python prints at the end of a `print()` call.