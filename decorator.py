def greater_first(func): 
    def wrap(a, b):
        if(a < b):
            a,b = b,a
        return func(a,b)
    return wrap

@greater_first
def minus(a,b):
    return a - b

@greater_first
def divide(a,b):
    return a / b

print(minus(1, 2))
