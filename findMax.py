def findMax(arr):
    maxValue = 0
    for num in arr:
        if(num > maxValue):
            maxValue = num
        
    print('Max value: ', maxValue)

findMax([8, 9, 1, 3])