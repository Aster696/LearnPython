# name = input('Enter your name: ');
# print(name);

num = 0

while(True):
    if(num%3==0 and num%5==0):
        print('Fizz Buzz')
    else:
        if(num%3==0):
            print('fizz')
        elif(num%5==0):
            print('Buzz')
        else:
            print(num)

    if(num==100):
        break
    num=num+1