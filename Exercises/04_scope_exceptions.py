## 1. Comprehension

listComp = [i for i in range(1, 6)]

print(listComp)
# print(i) # NameError: name 'i' is not defined. 

for i in range(1, 6):
    print(i)

print(i) # 5

# Accessing loop variable
# Comprehension - result in NameError
# for loop - returns the last iterator value.

## 2. try-except block

try:
    listComp[len(listComp)] 
except Exception as err:
    print(err) # list index out of range

print(err) # NameError: name 'err' is not defined
# exception variable is local to the except block