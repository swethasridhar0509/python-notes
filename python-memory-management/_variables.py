# Interned objects

a = 100
b = 100

print(a is b) # returns True

#non-Interned objects

a = -6
b = -6

print(a is b) # returns False 

# Float objects - non Interned

a = 1.20
b = 1.20

print(a is b) # False

# None is singleton

a = None
b = None

print(a is b) # True

# Small strings are interned

a = "hello"
b = "hello"

print(a is b) # True

a = "hello_world"
b = "hello_world"

print(a is b) # True


a = "hello world"
b = "hello world"

print(a is b) # False
print(a == b) # True