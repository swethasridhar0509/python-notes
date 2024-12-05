#********** Mutable object - functional argument *******************************

nums = [1, 2, 3, 4, 5]
print(id(nums)) # 140046009853504

def squares_in_place(numbers):
    print(id(numbers)) # 140046009853504
    for i, num in enumerate(numbers):
        numbers[i] = num ** 2
    return numbers 

res = squares_in_place(nums)
print(res, id(res)) # [1, 4, 9, 16, 25], 140046009853504

def squares_of_temp(numbers):
    temp = []
    for num in numbers:
        temp.append(num ** 2)
    return temp 

res = squares_of_temp(nums)
print(nums, id(nums)) # [1, 2, 3, 4, 5] 140046009853504
print(res, id(res)) # [1, 4, 9, 16, 25] 2707652734720

#********** Immutable object - functional argument *******************************

counter = 0
print(id(counter)) # 140705411199752

def increment(count):
    print(id(count)) # 140705411199752
    count += 1 
    return count 

ans = increment(counter)
print(counter, ans) # 0 1

def increment():
    global counter
    counter += 1 
    return counter 

ans = increment()
print(counter, ans) # 1 1

#********** Mutable default arguments **********************************

def increment(value, counter = []):
    counter.append(value)
    return counter

increment(2)
increment(3)
ans = increment(4)
print(ans)

def fibo_num(n, cache={0:1, 1:1}):
    if n not in cache:
        cache[n] = fibo_num(n - 1) + fibo_num(n - 2) 
    return cache[n]

res = fibo_num(10)
print(res)

#************ Augmented assignment **************************

# immutable

x = 100
y = x
x = x + 50 # creates a new object
# x += 50
print(y, x) # 100, 150

x = (1, 2)
y = x
x += (3, 4) # x = x + (3, 4)
print(x is y, x) # False

# Edge case

# x = (1, [2,3])
# y = x
# x[1] += [4,5]
# print(x, y)

# mutable

x = [1, 2, 3]
y = x
x = x + [1,2] # creates a new object
print(x, y)

x = [1, 2, 3]
y = x
x += [1,2] # in-place
print(x, y)



   




