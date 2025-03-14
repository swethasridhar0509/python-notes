def square(base):
    result = base ** 2
    print(f"Square of {base} : {result}")
    print(locals())

def cube(base):
    result = base ** 3
    print(f"Cube of {base} : {result}")
    print(locals())

print(dir()) # ['__builtins__', '__name__', 'cube', 'square']

square(20) 
# Square of 20 : 400
# {'base': 20, 'result': 400}

square(10)
# Square of 10 : 100
# {'base': 10, 'result': 100}

#print(result) # NameError: name 'result' is not defined

'''
Inference:
1. Trying to access local var: result outside throws NameError.
2. Avoid Naming conflicts. 
3. New scope for each function call.

'''