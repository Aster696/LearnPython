def count_vowels(str):
    vowels = 'aeiou'
    count = 0
    for char in str:
        if char.lower() in vowels:
            count += 1

    print('count: ', count)

count_vowels('Data Structures')