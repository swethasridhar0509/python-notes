## **Scope and Namespace**  
### Scope
- Scope refers to the area of a program where a variable, function or any object is accessible.
- It determines the **visibility** (accessible) and **lifetime** (existence in memory) of an object.
- Scopes helps with **naming conflicts**.
- There are 4 scopes in Python.
- The **location** at which the **object is created** is used associate it with a scope.
- In python, scopes are implemented using **namespace**.

### Namespace
- Namespace are dictionaries with name, object mapping.
- Each scope has a namespace with different lifetimes.
- When executing a program, python creates namespaces as required and deletes it later.
  

### **Types of Scope**  

1️. **Local Scope** (Inside a Function)  
   - Variables declared inside a function are **local** to that function.  
   ```python
   def my_function():
       x = 10  # Local scope
       print(x)

   my_function()
   print(x)  # ❌ Error: x is not defined outside
   ```

2️. **Enclosing Scope (Nonlocal Scope)**  
   - When a function is inside another function, the inner function can access the outer function’s variables (but not modify them without `nonlocal`).  
   ```python
   def outer():
       a = 5  # Enclosing scope

       def inner():
           nonlocal a  # Allows modification of enclosing variable
           a += 1
           print(a)

       inner()

   outer()  # 6
   ```

3️. **Global Scope** (Accessible Everywhere)  
   - Variables defined outside functions/classes are **global** and can be accessed inside functions using `global` if modification is needed.  
   ```python
   x = 100  # Global scope

   def my_function():
       global x
       x += 10  # Modifying global variable
       print(x)

   my_function()  # 110
   ```

4️. **Built-in Scope** (Python's Reserved Keywords & Functions)  
   - Functions like `print()`, `len()`, `sum()` are part of Python’s built-in scope and can be used anywhere.  
   ```python
   print(len([1, 2, 3]))  # Built-in function
   ```

---

### **Scope Lookup Rule (LEGB Rule)**
Python follows the **LEGB** rule to resolve variable names:  
1️. **Local** – Inside the function.  
2️. **Enclosing** – Variables from outer function scopes.  
3️. **Global** – Variables at the script/module level.  
4️. **Built-in** – Predefined Python functions.  

Example:  
```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # "local" (LEGB applies)

    inner()

outer()
```
- Python first checks **Local**, then **Enclosing**, then **Global**, and finally **Built-in**.

---

### **Common Scope Pitfalls**
 **Modifying Global Variables Without `global`**
```python
x = 5

def change():
    x += 1  #  UnboundLocalError (Python thinks x is local)
```
 **Fix**
```python
def change():
    global x
    x += 1
```
