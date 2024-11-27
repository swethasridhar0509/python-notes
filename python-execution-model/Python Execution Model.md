# Python Execution Model

Python uses a **hybrid execution model** that involves **compilation to bytecode** and **interpretation** by a virtual machine (PVM - Python Virtual Machine). 

---

### **1. Write the Source Code**

- Write the code in a `.py` file using a high-level programming language (Python syntax).

### **2. Compilation to Bytecode (Implicit)**

- The Python interpreter automatically compiles the source code into an intermediate format called **bytecode**.
- Bytecode is a low-level representation of your code but not machine code.
- **File Output**: Bytecode is often stored in `.pyc` files (compiled Python files) in the `__pycache__` directory.
- This step is **implicit**; the programmer doesn't need to run a separate compile command.

### **3. Bytecode Interpretation by PVM**

- The **Python Virtual Machine (PVM)** takes the bytecode and interprets it line-by-line.
- The PVM translates the bytecode into **machine code**, which the CPU executes.
- Bytecode interpretation happens dynamically at runtime.
- PVM acts as a layer that handles platform-specific execution.

---

## Python Interpreters

1. **CPython (Default interpreter)**
    - **Overview**: The standard implementation of Python, written in C.
    - **Execution**: Compiles Python source code into **bytecode** and executes it using the **Python Virtual Machine (PVM)**.
    - **Usage**: Comes pre-installed with Python (`python3` command).
2. **PyPy**
    - **Overview**: A faster alternative to CPython, using **Just-In-Time (JIT)** compilation.
    - **Execution**: Dynamically compiles frequently used bytecode into machine code during runtime, improving performance for long-running programs.
    - **Usage**: Requires separate installation.

        **JIT Compiler**: Component of Runtime Environments that converts bytecode into machine code duuring runtime.
        **Dynamic Compilation**: During execution, the JIT compiler translates frequently used parts of the intermediate code into native code.

3. **Jython**
    - **Overview**: An interpreter for Python, written in Java.
    - **Execution**: Translates Python code into **Java bytecode** and runs it on the **Java Virtual Machine (JVM)**.
    - **Usage**: Popular in environments requiring Python-Java interoperability.