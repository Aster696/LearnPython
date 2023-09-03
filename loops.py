# For loop
# ninjas = ['ryu', 'crystal', 'yoshi', 'ken'];

# for ninja in ninjas:
#     print(ninja);

# for ninja in ninjas:
#     if ninja == 'yoshi':
#         print(f'{ninja} - is black belt');
#     else:
#         print(ninja);

# for ninja in ninjas:
#     if ninja == 'yoshi':
#         print(f'{ninja} - is black belt');
#         break;
#     else:
#         print(ninja);


# while loop
age = 25;
num = 0;

# while num < age:
#     print(num);
#     num += 1;

while num < age:
    if num == 0:
        num += 1;
        continue;
    if num % 2 == 0:
        print(num)
    if num > 10:
        break;
    num += 1;
