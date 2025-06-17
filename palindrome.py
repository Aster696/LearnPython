# palindrome means the name or number should be same in reverse as well eg: madam

def palindrome(str):
    return str == str[::-1]

print(palindrome('madam'))