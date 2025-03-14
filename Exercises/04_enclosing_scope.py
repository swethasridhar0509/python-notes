def outer_add_nums():
    count = 0
    nums = []

    def inner_add_nums(num):
        nonlocal count
        count += 1
        nums.append(num)
        print(nums, count)
    
    print(inner_add_nums.__closure__)
    return inner_add_nums

x = outer_add_nums() # x holds ref to inner_add_nums

x(10)
x(12)
x(14)

# [10] 1
# [10, 12] 2
# [10, 12, 14] 3

'''
Inference:
1. Use nonlocal to modify immutable data type inside enclosed func
2. the local scope of outer func() is the enclosing scope of inner func()
2. __closure__ to identify the existence of enclosing vars
'''