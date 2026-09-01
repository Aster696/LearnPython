def square(num):
    return num * num

def cube(num):
    return num * num * num

def operations(nums, operation):
    for num in nums:
        print(operation(num));

operations([3,5,7], cube)
