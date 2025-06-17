def remove_dublicate(str, arr):
    check = set()
    result = ''
    for char in str:
        if char not in check:
            check.add(char)
            result += char
    
    return result

print(remove_dublicate('asteralister', []))