## Data Types
- Data type defines the **type of data** stored and **operations** that can be performed on the data.
- **Purpose:** Ensure valid operations are performed and optimize memory usage.

## Python Numbers
- Python supports 3 types of numbers - **Integers, Floating-point numbers,** and **Complex** **numbers**.
- **Integers:** Numbers whose fractional part is 0. Includes Positive numbers, Negative numbers and zero. **Ex:** 1, 0, -1.
- **Floating-point Numbers:** Numbers with a decimal point or in scientific notation. **Ex:** 3.14 and 10e3.
- **Complex Numbers:** Number with real and imaginary part. **Ex:** 3 + 4j 

## Python Integers - int
1. The built-in data type `int` represents **Integers**
2. In python, integer has no limit, the only constraint is the memory.
3. Use underscores for long numbers. **Ex:** 1_00_000
### Creating Integers
1. Directly assigning integer literals to variables. **Ex:** `x = 100`
2. Using `int()` **Ex:** `x = int(100)`
3. `type(x)` returns `<class 'int'>`
### int() built-in function
1. The `int()` function converts **values** into an **integer**.
2. Returns an **integer object**.
3. **Syntax:** `int(x, base=10)`
4. **Parameters:** 
   - **x** - value to be converted. Accepts interger literals, float, string.
   - Malformed string will throw `ValueError`
   - **base** - Number system base. Used only with string values.
   - Used to convert numbers from other number system to integer.

### Use cases of int
1. Counting items
2. Indexing elements in collections
3. Performing artihmetic operations
4. Representing numerical data in various bases
