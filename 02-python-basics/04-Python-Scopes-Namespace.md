## **Scope and Namespace**  
The term **Name** refers to the identifiers of variables, constants, function, classes, or any python objects.  

### Scope
- **Scope of a name** refers to the area of the program where a name is **accessible**.
- Scope determines the **lifetime** (how long it is stored in memory) and **visibility** (accessibility) of a name.
- There are **4** scopes - Local, Global, Enclosing and built-in
- Python uses the **location** of assignment or definition to associate a name with a scope.

### Advantages of Scope
1. Avoid naming conflicts.
2. Restricts bad usage of global names.
3. Better code organization.
  
### Namespaces
- Namespaces are containers with names and objects associated with the names.
- Namespaces are implemented as dictionaries.
- The concept of scope is implemented using namespaces.
- Namespaces can also be manually created by creating modules and importing it.
- Python creates namespaces as required an deletes it later.
  
### LEGB Rule

- Python uses the **LEGB rule** to resolve variables in a program.
- It first looks for the variable in the local scope, then enclosing scope, then global and finally builtin scope.
- If the **variable is found**, the first occurence is returned else throws `NameError`.

## Types of scope and namespaces

### Functions: The Local Scope

1. **Functions & Local Scope:** Local Scope (namespace) or function scope is created when a function is called.
2. **Creation:** A new local scope is created for each function call.
3. **Lifetime:** Local scope is destroyed when the function returns.
4. **Local variables:** Parameters and variables assigned in the function exist only within the local scope associated with the function call.
5. **NameError:** Trying to access the local variables outside the function throws `NameError`.
6. **Avoiding Naming conflicts:** Seperate local scopes allows different functions to use the same variable names without conflict.
7. `locals()`: Returns a dictionary of the current local namespace.

``` python
def square(base):
    result = base ** 2
    print(f"Square of {base} : {result}")
    print(locals()) # Access local namespace

# using the same variable names due to separate local scope
def cube(base):
    result = base ** 3
    print(f"Cube of {base} : {result}")
    print(locals())
```
```python
square(20) # new scope for each function call; variables are not retained.
# Square of 20 : 400
# {'base': 20, 'result': 400}

square(10)
# Square of 10 : 100
# {'base': 10, 'result': 100}

print(result) # NameError
'''
Inference:
1. Trying to access local var: result outside throws NameError.
2. Avoid Naming conflicts. 
3. New scope for each function call.

'''

```
### Nested Functions: Enclosing Scope

1. **Enclosing Scope (or) Nonlocal Scope:** An enclosing scope is created when there is a closure (function nested within a function).
2. The outer function's local scope is also the inner function's enclosing scope.
3. Existence of enclosing function is determined by the `__closure__` attribute.
4. **Lifetime:** Enclosing scope is destroyed when the function returns.
5. **Nonlocal variables:** Parameters and variables assigned in the outer function are called nonlocal variables.
6. Nonlocal variables are accessible from the inner function but modification is not allowed.
7. Using `nonlocal` statement modify enclosing variables.  
8. **NameError:** Trying to access the local variables outside the function throws `NameError`.

``` python
def outer_add_numbers():
    numbers = []
    count = 0
    # outer func() - local scope
    # inner func() - enclosing scope
    
    def inner_add_numbers(num):
        numbers.append(num)
        print(numbers, count)
        # nonlocal count
        count += 1 # throws unboundlocalerror  
    
    return inner_add_numbers
    
add_num = outer_add_numbers()
add_num(12) # [12], 0
add_num(13) # [12, 13], 1
```



