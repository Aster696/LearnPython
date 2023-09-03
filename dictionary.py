names = {"name": 'aster', "email": 'a@gmail.com', "password": 1234}

# print(names)
# print(names["name"])

# check if key exist
# print("address" in names)

# print(names.keys())

# print(list(names.keys()))

# print(names.values())

# val = list(names.values())

# print(val.count('aster'))

# add new key
# names['address'] = 'a@gmail.com'
# val = list(names.values())
# print(names, val.count('a@gmail.com'))

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

def displayBelts():
    for key, value in ninja_belts.items():
        print(f'ninja name {key} & ninja belt {value}')

displayBelts()
