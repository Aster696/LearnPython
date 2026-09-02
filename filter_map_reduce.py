from functools import reduce

nums = [2, 23, 4, 8, 7, 9, 6]

even = list(filter(lambda n: n % 2 == 0, nums))
double = list(map(lambda n: n * 2, nums))
sum = reduce(lambda a,b: a + b, double)

print("Even", even)
print("Double", double)
print("Sum", sum)