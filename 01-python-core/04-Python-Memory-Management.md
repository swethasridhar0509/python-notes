## **Memory Model**

The **operating system** allocates **virtual memory** for each program. This virtual memory is divided into:

### **Heap Memory**

- The **heap** is used for **dynamic memory allocation** when creating objects.
- All Python objects and data structures are stored in a private heap managed by Python Memory Manager.
- Python uses a **garbage collector** to automatically manage memory allocation and deallocation in the heap.

### **Stack Memory**

- Stores **local variables** and **function call information**.
- Every time a function is called, a new **stack frame** is created, which includes,
    1. local variables
    2. function arguments
    3. return address
- When the function finishes executing, the stack frame is removed.

## **Memory Management in Python**

- Memory management refers to the process of efficiently allocating and deallocating memory during the execution of a program.
- In Python, memory management involves:
    1.  Tracking memory usage
    2. Allocating space for objects and 
    3. Freeing up memory when objects are no longer needed.
- In C/C++, users are responsible for memory management.
- Python does automatic memory management using **reference** **counting** and **garbage collection**.

### **PyObject**

- Every Python object, whether a string, list, number, or function, is represented by a `PyObject` structure in the Heap.
- **PyObject** is the internal representation of every Python object.
- Attributes include,
    1. Type information.
    2. Actual value
    3. Reference count of the object.
- **Role** - object representation & type identification.

### **Reference Count**

- Reference counting is a memory management technique that tracks the references to an object in the heap.
- Each Object represented using PyObject has a reference count attribute.
- When a new reference to an object is created, the count is increased by 1.
- When a reference is deleted, the count decreases by 1.

### **Garbage Collector**

- Garbage collection is a memory management technique that frees memory in the heap by clearing unused objects.
- A garbage collector runs periodically to check for any objects whose count is 0. If so, the GC clears the object from the memory.
- Built-in module **GC** can be used to interact with the Garbage collector.
- GC clears cyclic references (two objects referencing each other preventing the count from dropping to zero)


## **Memory & Race Conditions**

- Memory is a shared resource.
- Two processes trying to modify the shared resource simultaneously without proper synchronization could lead to unintended bugs. This is called race conditions.
- Race conditions often occur in multithreaded programs, i.e., a program that spins up multiple threads of execution at once.
- If two threads try to access data at once, the program might crash.
- To avoid this, it’s best to write thread-safe code.
- In thread-safe code, shared resources are protected by a mutex.
- One form of a mutex is a lock, which locks the shared resource. When one thread is accessing the shared resource in memory, that resource is said to be locked.

## **Global Interpreter Lock**

- CPython’s approach to thread safety is GIL, rather than use a bunch of locks, the GIL locks the interpreter.
- The Global Interpreter Lock (GIL) in Python is a mechanism that ensures only one thread executes Python bytecode at a time.
- **Purpose**: Prevents race conditions by allowing only one thread to execute Python bytecode at any given time.
- **Implementation**: Acts as a mutex, locking the interpreter to ensure thread safety during memory management.
- **CPU-bound Tasks**: Limits performance in CPU-intensive multi-threaded programs, as threads cannot run in true parallelism.