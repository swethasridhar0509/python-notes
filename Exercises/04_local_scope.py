################## Built-in scope ######################################

print = {"name": "john doe"}
print(dir())

# print is assigned a dict.
# TypeError: 'dict' object is not callable.

################## global scope ######################################

x = "global x" 

def level_one():
    return x

print(level_one) # return global x

# RULE: Lookups happens at runtime, location is decided at compile time.
# 1. No assignment for x in local scope, x present in global scope is used.
# 2. Avoid naming conflicts, using x in both local and global scope.

################## Local Scope #######################################

x = "global x" 

def level_two(v):
    # print(x) # Trying to access x before assignment throws UnboundLocalError
    if v:
        x = "local x"
    return x

print(level_two(True)) # return local x
print(level_two(False)) # throws UnboundLocalError

# Python compiles the function before execution and creates a function object.
# Detects Assignment statement and marks x as local variable.
# if v = False, there is no assignment, hence the error UnboundLocalError
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

def square(base):
    result = base ** 2
    print(f"Square of {base} : {result}")

def cube(base):
    result = base ** 3
    print(f"Cube of {base} : {result}")

# New scope for each function call.
square(20) # Square of 20 : 400

# New scope for each function call.
square(10) # Square of 10 : 100

# Trying to access local var: result outside throws NameError.
print(result) # NameError: name 'result' is not defined

################## Enclosing Scope #######################################

x = "global x"

def level_three():
    def inner(y):
        return x, y, z
    z = "outer z"
    print(inner.__closure__)
    print(inner.__globals__)
    return inner("y arg")

print(level_three()) # "global x", "y arg", "outer z"

# In the end inner() is called.
# y - passed as an arg, found in the local scope.
# x - not in local and enclosing scope, found in global.
# z - not defined in the local scope, found in the enclosing scope.
# z is assigned before invoking inner()