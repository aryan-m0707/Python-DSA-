def linearSearch(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1

array= [1,2,3,4,8,7,9]
target=7
result=linearSearch(array,target)
if result == -1:
    print("Target Not Found")
else:
    print("Element found at index",result)