# def fact(num):
#     res = 1
#     for i in range(1, num+1):
#         res = res * i

#     return res

def fact(num): 
    if num == 1:
        return 1
    return num * fact(num - 1) 

print(fact(5))