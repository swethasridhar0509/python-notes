import random

name = "John"
age = 20

def greet():
    name = "Jane" # name is a local var now.
    global age
    age += 30 # UnboundLocalError: cannot access local variable 'age'
    print(f"Hello {name} {age}!")
    print(locals()) # {'name': 'Jane'}

greet() 
# Hello Jane!

print(f"Global Variables: {globals()}") 

'''
Global Vars: {'__name__': '__main__', 
'__builtins__': <module 'builtins' (built-in)>, 
'random': <module 'random'>,
'name': 'John', 'age': 50, 
'greet': <function greet at 0x000002178D4004A0>}
'''

