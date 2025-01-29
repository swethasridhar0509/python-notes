## **Python Execution Model**

- Python uses a **hybrid execution model** that involves compiling to bytecode and interpreting it by a virtual machine (Python Virtual Machine) line-by-line.
- Cpython is the default interpreter and is written in C.
- **Steps in Execution:**
    
    **1.** Write the Source Code
    
    **2.** Compilation to Bytecode (Implicit), stored in the **pycache** folder.
    
    **3.** Bytecode Interpretation by **Python Virtual Machine (PVM).**

## **Python Interpreters**

**CPython (Default interpreter)**
- **Overview**: The standard implementation of Python, written in C.
- **Execution**: Compiles Python source code into **bytecode** and executes it using the **Python Virtual Machine (PVM)**.
- **Usage**: Comes pre-installed with Python (`python3` command).

**PyPy:**  A faster alternative to CPython, using **Just-In-Time (JIT)** compilation.

**Jython:** An interpreter for Python, written in Java. Translates Python code into **Java bytecode** and runs it on the **Java Virtual Machine (JVM)**.


## **Responsibilities of Python Interpreter**

- **Reading and Parsing Code**: It reads the Python source code and parses it into a format that can be processed.
- **Compiling to Bytecode**: The interpreter compiles the parsed code into bytecode, a platform-independent intermediate representation.
- **Executing Bytecode**: The bytecode is then executed by the Python Virtual Machine (PVM), which translates it into machine-level instructions for the host system.
- **Managing Memory**: It handles memory allocation and garbage collection.
- **Error Handling**: The interpreter detects and reports errors in the code.