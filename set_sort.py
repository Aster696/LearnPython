nums = [2, 4, 5, 6, 765, 4, 76, 0, 1, 3, 7]
names = ['banana', 'Banana' ,'Apple', 'abc', 'dkb', 'Apple']

# sort sets elements in order
# print(sorted(nums))
# print(sorted(names))

# set create new set which does not have dublicate data
# print(set(nums))
# print(set(names))

# use set and short
# print(sorted(set(nums)))
# print(sorted(set(names)))

# short and set in dictionary
ninja_belts = {}

while(True):
    ninja_name = input('Enter ninja name: ')
    ninja_belt  = input('Enter ninja belt name: ')

    ninja_belts[ninja_name] = ninja_belt

    another = input('Add another? (y/n): ')
    if(another == 'y'):
        continue
    else:
        break

def belt_count():
    belts = list(ninja_belts.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

belt_count()
