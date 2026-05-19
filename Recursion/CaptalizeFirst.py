def capitalizeFirst(arr):

    result = []
    if len(arr) == 0:
        return result
    
    result.apped(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])
print(capitalizeFirst(['car', 'taco', 'banana']))