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
In [2]: cost = 12.25
In [3]: quantity = 5
In [4]: print("The cost of", quantity, "sodas is:", cost)
The cost of 5 sodas is: 12.25

In [14]: nums = [1, 2, 3]
In [15]: digit = 10
In [16]: _dict = {"yes" : 1, "no" : 0}

In [17]: print(nums, digit, _dict, len)
[1, 2, 3] 10 {'yes': 1, 'no': 0} <built-in function len>
```

- `sep = " "` **(optional keyword argument) [defaults to single space]** - It is used to separate multiple arguments. It can accept string or None (calls default). To suppress `sep` use `""` .

```python
# Using Default separator
In [5]: fname = "John"
In [6]: print("First Name:", fname)
First Name: John

# To introduce line breaks
In [9]: print("Hello", "World", sep="\n")
Hello
World

#custom separator for dates
In [10]: print("05", "09", "2002", sep="-")
05-09-2002
```

- `end = "\n"` **(optional Keyword argument)[defaults to newline]** - appends a string to the end. It could be used to prevent line breaks. It accepts string or None.

```python
# Default behavior
In [14]: fname = "John"
In [15]: lname = "Doe"
In [16]: print("Full Name:", fname);print(lname)
Full Name: John
Doe

# using end to prevent line break
In [20]: print("Full Name:", fname, end=" ");print(lname)
Full Name: John Doe
```

```python
In [22]: nums = [1, 2, 3]
In [23]: for num in nums:
    ...:     print(num)
1
2
3

In [24]: for num in nums:
    ...:     print(num, end=" ")
1 2 3
```

- Calling `print()` - results in a blank line with only one newline character from the end argument. This can be used to introduce vertical space between objects.
- `file = sys.stdout` **(optional Keyword argument)[defaults to standard output `stdout`]** - print write the output to a stream. by default the standard output stream (console), It can be changed using the file arguments. The output can be redirected to any file.

```python
In [26]: import sys

In [27]: print("Printing to a File", file=sys.stdout)
Printing to a File

In [28]: print("Printing to a File", file=open("file.txt", "w"))
```

- Any errors are directed to the standard error stream - stderr.
- `flush = False` **(optional Keyword argument)[defaults is False] -** determines whether to forcibly flush the stream. It can be used to avoid buffering I/O operations.
- **Streams**  buffers (stores the output in some register) output until `'\n'` character (line buffering) or the buffer is 4096 characters (block buffering). Then the stream is flushed. Output is printed.
- Buffered output can cause delays. Flushing will be helpful in real-time updates.

```python
# Default the output will be printed all at once after 5 secs.
In [50]: import time
In [51]: for i in range(1, 11):
    ...:     print(f"{i}...", end = " ")
    ...:     time.sleep(0.5)
    ...:
1... 2... 3... 4... 5... 6... 7... 8... 9... 10...
```

```python
# Buffering is avoided, numbers are printed one after another
# with 0.5 secs gab in between. 
In [52]: for i in range(1, 11):
    ...:     print(f"{i}...", end = " ", flush=True)
    ...:     time.sleep(0.5)
    ...:
1... 2... 3... 4... 5... 6... 7... 8... 9... 10...
```

## Input() - Reading data

- The `input()`  is used to obtain data from the users. It takes input from the user and returns it.
- It passes the execution of the program and allows the user to type.
- Once the Enter key is pressed, the input is collected as a string, excluding the new line character.
- Any text (optional) added between the `()`  is passed to the optional **prompt** argument and will be displayed as a prompt.

```python
In [1]: name = input("Enter your name: ")
Enter your name: A
In [2]: name --> Out[2]: 'A'
```

## Type Casting the input

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
In [6]: number + 50 --> Out[6]: 150
In [10]: type(number) --> Out[10]: int
```

```python
In [7]: amount = float(input("Enter total amount: "))
Enter total amount: 50.90
In [9]: type(amount) --> Out[9]: float
```

## Examples

- Taking multiple inputs in a single line.
- `split()` separates characters in a string with space as default.

```python
In [72]: a, b, c = input().split()
21 32 43
In [73]: print(a, b, c) # 21 32 43

# packing input into a list
In [74]: a = input().split()
32 21 76
In [75]: a --> Out[75]: ['32', '21', '76'] # list

#converting to int
In [3]: a = list(map(int, input().split()))
12 32 43
In [4]: a --> Out[4]: [12, 32, 43]

# getting remaining values into a list
In [77]: a, *b = input().split()
12 13 14

In [78]: print(a, b) # 12 ['13', '14']
```

- Taking input from a known range.

```python
In [80]: nums = []
In [81]: for i in range(1, 4):
    ...:     num = input()
    ...:     nums.append(num)
1
2
3
In [82]: nums --> Out[82]: ['1', '2', '3']
```

- Taking input from a unknown range.

```python
import sys
for line in sys.stdin:
		user_input = line.split() 
```