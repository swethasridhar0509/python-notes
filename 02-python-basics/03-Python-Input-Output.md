## Input / Output

- Programs need to communicate with the users, whether to get data or to provide results of the program.
- Built-in function `input()` - captures user input from the keyword.
- Built-in function `print()` - display output in the console.

## Print() - Displaying Output

- `print()` is a built-in function that prints the given object(s) to the standard output or text stream file.
- Common use cases - debugging and displaying output.
- Print was a statement in Python 2.
- **Syntax:**  `print(*args, sep=' ', end='\n', file=sys.stdout, flush=False)`
- **Returns:** None, prints string representation of the objects passed.
- `*args` - The objects to be printed are passed to the `print()` using `*args` . It allows a function to accept any no. of. positional arguments as a tuple. It can be zero, one or more.
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

- `sep = " "` **(optional keyword argument) [defaults to single space]** - It is used to separate multiple arguments. It can accept string or None (calls default). To suppress `sep` use `""` .

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

- `end = "\n"` **(optional Keyword argument)[defaults to newline]** - appends a string to the end. It could be used to prevent line breaks. It accepts string or None.

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

- Calling `print()` - results in a blank line with only one newline character from the end argument. This can be used to introduce vertical space between objects.
- `file = sys.stdout` **(optional Keyword argument)[defaults to standard output `stdout`]** - print write the output to a stream. by default the standard output stream (console), It can be changed using the file arguments. The output can be redirected to any file.

```python
import sys

# printing to a standard output stream
print("Printing to a File", file=sys.stdout) # Printing to a File

# printing to a file stream
print("Printing to a File", file=open("file.txt", "w"))
```

- Any errors are directed to the standard error stream - stderr.
- `flush = False` **(optional Keyword argument)[defaults is False] -** determines whether to forcibly flush the stream. It can be used to avoid buffering I/O operations.
- **Streams**  buffers (stores the output in some register) output until `'\n'` character (line buffering) or the buffer is 4096 characters (block buffering). Then the stream is flushed. Output is printed.
- Buffered output can cause delays. Flushing will be helpful in real-time updates.

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

- The `input()`  is used to obtain data from the users. It takes input from the user and returns it.
- It passes the execution of the program and allows the user to type.
- Once the Enter key is pressed, the input is collected as a string, excluding the new line character.
- Any text (optional) added between the `()`  is passed to the optional **prompt** argument and will be displayed as a prompt.

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

## Examples

- Taking multiple inputs in a single line.
- `split()` separates characters in a string with space as default.

```python
a, b, c = input().split()
# 21 32 43
print(a, b, c) # 21 32 43
```

- Packing input into a list.

```python
a = input().split()
# 32 21 76
print(a, type(a)) # ['32', '21', '76'], <class 'list'>
```

- Packing input into a list of numbers.

```python
a = list(map(int, input().split()))
# 12 32 43
print(a, type(a[0])) # [12, 32, 43], <class 'int'>
```

- Getting remaining values into a list.

```python
a, *b = input().split()
# 12 13 14
print(a, b) # 12 ['13', '14']
```

- Taking input from a known range.

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

- Taking input from an unknown range.

```python
import sys
for line in sys.stdin:
    user_input = line.split() 
```