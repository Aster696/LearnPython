def outer():
    print("Outer function")
    def inner(num):
        print("Inner function", num)
    
    return inner

show = outer()
show(6)