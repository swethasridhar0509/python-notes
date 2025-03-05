## Input / Output
- **functions** - Resuable block of code that performs a action or task.
- **Built-in function** - Predefined functions that are built within the **Python Interpreter**. Does not require importing modules.
- **Input/Output** - Programs need to communicate with the users, whether to get data or to provide results of the program.
- Built-in function `input()` - captures user input from the keyword.
- Built-in function `print()` - display output in the console.

## Print() - Displaying Output

- **Built-in function** that prints the given object(s) to the **standard output stream (console)** or **file**.
- **Use cases** - debugging and displaying output.
- Print was a statement in Python 2.
- **Syntax:**  `print(*object(s), sep=' ', end='\n', file=sys.stdout, flush=False)`
- **Returns:** None, prints string representation of the objects passed.
### Parameters
1.  `*object(s)` - The objects to be printed are passed to the `print()` using `*objects` parameter . `*args` allows a function to accept any no. of. positional arguments as comma separated values. It can be zero, one or more.
  - Internally print calls `str()` of all the objects.
  - Finally all the objects are concatenated as a single string with single spaces separating them.

```python
# prints the str representation of the objects passed
_list = [1, 2, 3]
_dict = {1: True, 0: False}
_int = 10 
_float = 5.5
print(_list, _dict, (_int + _float), print) 
# [1, 2, 3] {1: True, 0: False} 15.5 <built-in function print>
```
2. `sep = " "` **(optional keyword argument) [defaults to single space]**
- Accepts string or None (default).
- Appends the string to the end of each object passed to the `print()`.
- Used to separate multiple arguments.
- To suppress `sep` use `""`

```python
# Using Default separator
fname = "John"
print("First Name:", fname) # First Name: John

# To introduce line breaks
print("Hello", "World", sep="\n")
# Hello
# World

# Custom separator for dates
print("05", "09", "2002", sep="-") # 05-09-2002
```

3. `end = "\n"` **(optional Keyword argument)[defaults to newline]**
- Accepts string or None (default).
- Appends the string atlast.
- Used to prevent line breaks.
- Calling `print()` - results in a blank line with only one newline character from the end argument. This can be used to introduce vertical space between objects.

```python
fname = "John"
lname = "Doe"
print("Full Name:", fname)
print(lname) # Full Name: John
             # Doe

# using end to prevent line break
print("Full Name:", fname, end=" ")
print(lname) # Full Name: John Doe
```

```python
nums = [1, 2, 3]
for num in nums:
    print(num)
# 1
# 2
# 3

for num in nums:
    print(num, end=" ") # 1 2 3
```

4. `file = sys.stdout` **(optional Keyword argument)[defaults to standard output `stdout`]**
- Accepts file object.
- Writes the output to a stream.
- by default the standard output stream (console), It can be changed using the file param.
- The output can be redirected to any file.
- Any errors are directed to the standard error stream - stderr.

```python
import sys

# printing to a standard output stream
print("Printing to a File", file=sys.stdout) # Printing to a File

# printing to a file stream
print("Printing to a File", file=open("file.txt", "w"))
```

5. `flush = False` **(optional Keyword argument)[defaults is False] -**
- Accepts `True` or `False`.
- Determines whether to forcibly flush the stream.
- It can be used to avoid buffering I/O operations.
- **Streams**  buffers (stores the output in some register) output until `'\n'` character (**line buffering**) or the buffer is 4096 characters (**block buffering**). Then the stream is flushed. Output is printed.
- **Usecase** - Buffered output can cause delays. Flushing will be helpful in real-time updates.

```python
# Default the output will be printed all at once after 5 secs.
import time
for i in range(1, 6):
    print(f"{i}", end="...")
    time.sleep(0.5)
 # ... 2... 3... 4... 5...
```

```python
# Buffering is avoided, numbers are printed one after another
# with 0.5 secs gab in between. 
import time
for i in range(1, 6):
    print(f"{i}", end="...", flush=True)
    time.sleep(0.5)
# ... 2... 3... 4... 5...
```

## Input() - Reading data
- Takes keyboard input from the user and returns a **string**.
### Parameters
- **prompt(optional)** - Placeholder text to be displayed. Any text (optional) added between the `()`  is passed to the optional **prompt** argument and will be displayed as a prompt.
### Working
- It passes the execution of the program and allows the user to type.
- Prompts the user for a input, if prompt is present.
- Once the Enter key is pressed, the input is collected as a string, excluding the new line character.

```python
_string = input("Enter input string: ")
# Enter input string: A
print(_string) # 'A'
```

## Type Casting the input

- The `input()` reads and returns the user’s input as a string.
- If numbers are entered, it will be treated as a string.
- To handle this, covert the input to the appropriate type.

```python
_int = input("Enter a random number: ")
# Enter a random number: 100
print(type(_int))  # <class 'str'> 
print(_int + 50) # TypeError: can only concatenate str (not "int") to str

_int = int(input("Enter a random number: "))
# Enter a random number: 100
print(type(_int)) # <class 'int'>
print(_int + 50)  # 150
```

```python
_float = float(input("Enter float value: "))
# Enter float value: 50.90
print(_float, type(_float)) # 50.9 <class 'float'>
```
## Common pitfalls
 - TypeError: can only concatenate str (not "int") to str.
 - ValueError: passing string to int() or float(). Use try catch.

## Reading Multiple Inputs

1. **Taking multiple inputs in a single line**
  - Use `list()`, `split()`, `strip()` to read multiple values in a single string and append it to a list.
  - Use list comprehension or `map()` for type conversions.
    ### Examples
    
    ```python
    a, b, c = input().split()
    # 21 32 43
    print(a, b, c) # 21 32 43
    ```
    ```python
    a = [s.split() for s in input().split()]
    # 32 21 76
    print(a, type(a)) # ['32', '21', '76'], <class 'list'>
    ```
    ```python
    a = list(map(int, input().split()))
    # 12 32 43
    print(a, type(a[0])) # [12, 32, 43], <class 'int'>
    ```

    ```python
    # Getting remaining values into a list.
    a, *b = input().split()
    # 12 13 14
    print(a, b) # 12 ['13', '14']
    ```
    
    
3. **Taking multiple inputs line-by-line**
  - For a known range, use a for loop and read line by line.
  -**Example:**
      ```python
      nums = []
      for i in range(1, 4):
          num = input()
          nums.append(num)
      # 1
      # 2
      # 3
      print("nums:", nums) # nums: ['1', '2', '3']
      ```

  - For a unknown range, use a for loop with sys.stdin.
  - **Example:**

    ```python
      import sys
      for line in sys.stdin:
          user_input = line.split() 
      ```
  ## Third-party packages
  - `getpass` module - Useful for senstive inputs like password, emails and API Keys. Does not print keyboard entries on the screen.
  - `pyInputplus` module - Useful for Input validation. 
