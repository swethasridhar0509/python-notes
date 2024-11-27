# Python Memory Model

### **Memory Model in Python**

The **operating system** allocates **virtual memory** for each program. This virtual memory is divided into several segments:

1. **Code Segment**: Contains the machine code instructions (compiled program).
2. **Global Segment**: Stores global variables and constants.
3. **Heap**: Used for dynamic memory allocation.
4. **Stack**: Stores local variables and function call information.

---

### Stack Memory

**Structure**

- The **stack** follows a **Last In, First Out (LIFO)** structure.
- The most recent function call is placed on top of the stack, and when a function returns, the associated memory is popped off.

**What Goes in the Stack**

- **Local variables**: Variables declared within functions or methods.
- **Function call information**: Details about function execution such as the return address and arguments.
- **Function parameters**: Arguments passed to a function

**Characteristics**

- Automatic memory management.
- Limited Size

```python
def add(a, b):
    result = a + b  # 'result' is stored in stack
    return result

x = 10  # 'x' is stored in stack
y = 20  # 'y' is stored in stack
print(add(x, y))  # Function call and parameters stored in stack
```

---

### Heap Memory

**Structure**

- The **heap** is a region of memory used for **dynamic memory allocation**.
- Unlike the stack, it allows for flexible memory management during program execution.

**What goes in the Heap**

- **Objects**: Any object created dynamically, such as lists, dictionaries, and class instances.

**Characteristics**

- **Dynamic Memory Allocation**: Memory in the heap is allocated at runtime. Python uses **garbage collection** (through reference counting and cycle detection) to automatically manage heap memory.
- Flexible in size.

```python
def create_person(name, age):
    person = {"name": name, "age": age}  # Dictionary object stored in heap
    return person

name = "Alice"  # String reference in stack, string value in heap
age = 30        # Integer reference in stack, integer value in heap
person = create_person(name, age)  # Person object reference in stack, object in heap
print(person)
```

---

- **Global Segment** stores global variables, constants, and references to objects used across the program.
- They are stored in memory in the **global symbol table**.
- **Code Segment** stores the compiled bytecode of your program.

---