# Python Variables & Memory Management

### Variable

- A variable is a **named reference** to a memory location that stores data.
- **Example**: `x = 10` assigns the value `10` to the variable `x`.

### Purpose

- Eliminates the need to handle memory addresses directly.
- Increases code reusability & readability.

---

### Variable Creation

### **In C**:

1. **Memory Allocation**:
    - Example: `int x = 10;`
    - The compiler allocates memory in the **stack**.
    - Memory size depends on the data type (`int`, `float`, etc.).
    - The memory holds the value `10`, and `x` stores the memory address.

### **In Python**:

1. **Memory Allocation**:
    - Example: `x = 10`
    - Python creates an **integer object** (`10`) in the **heap**.
    - This object is an instance of the **PyObject** structure.
    - Reference x to the object is stored in the **stack**.
2. **Dynamic Typing**
    - Type is associated with the object, not the reference.
    - Example: `x = 20` (integer), then `x = "hello"` (string).

3**.   PyObject's Role**

- **Type Identification -** tracks the type of the object (e.g., `int`, `str`).
- **Reference Count -** Tracks how many variables reference the object.
- **Value** - holds the value.
- **Memory Management -** Helps with garbage collection when reference count drops to `0`.

---

### Variable Assignment Cases

### **Case 1: Assigning a New Value**

**In C**:

- Example: `x = 20`
- Updates the existing memory location for `x` with the new value (`20`).
- No new memory is allocated.

**In Python**:

- Example: `x = 20`
- A new integer object (`20`) is created in the **heap**.
- `x` now references this new object.
- Reference count for the old object (`10`) decreases. If it reaches zero, the memory is freed.

---

### **Case 2: Copying References or Values**

**In C**:

- Example: `y = x`
- Allocates new memory for `y` and copies the value of `x` into it.
- `x` and `y` are independent; changes to one do not affect the other.

**In Python**:

- Example: `y = x`
- `y` references the same object as `x`.
- No new object is created.
- Reference count for the object increases.

---

### **Case 3: Assigning the Same Value to Another Variable**

**In C**:

- Example: `z = 20`
- Allocates new memory for `z` and stores `20` in it.
- `z` is independent of any other variables with the same value.

**In Python**:

- Example: `z = 20`
- Python reuses the existing object (`20`) if available.
- `z` references the same object as `x` (or any variable already holding `20`).
- Reference count for the object increases.

---

### **Case 4: Modifying the Value**

**In C**:

- Example: `x = x + 5`
- Fetches `x`'s value from memory, computes the result, and updates `x`'s memory location with the new value.

**In Python**:

- Example: `x = x + 5`
- Fetches the object `x` references, computes the result (`15`).
- A new object (`15`) is created in the **heap**.
- `x` is updated to reference the new object.
- Reference count for the old object decreases.

---

### Case 5: Re-assignment

**In C:**

- Updates existing memory directly.

**In Python**

- Creates a new object and updates reference.

---

### Interning

1. Interning is a memory optimization technique that **improves performance** and **optimizes memory usage** by reusing immutable objects. 
2. **Integer** **Interning** - small digits within the range (-5 to 255) are pre-cached for reuse.
3. **String** **Interning** - small strings (length < 20), strings with underscore and identifiers are interned for reuse. 
4. Use `sys.intern()` to manually intern strings or numbers.

---

### “==” vs is

|  | **`==` (Equality)** | **`is` (Identity)** |
| --- | --- | --- |
| **Function** | Compares the **value** of two objects. | Compares the **memory address** of two objects. |
| **Explanation** | Returns `True` if the values of two objects are equal.  | Returns `True` if two objects refer to the same memory location. |
| **Key** **differences** | Works by calling the `__eq__()` method of the object. | Used for checking `None` or interning behavior |
| **Example** | `a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # true` | `print(a is b) # false` |

---

### None in Python

- `None` is a singleton, and immutable object.
- All instances of `None` share the same memory address.
- Use `is` for comparisons with `None` for optimal performance.