def binarySearch(arr,tar):
    low=0
    high=len(arr)-1
    while low<=high :
        mid=(low+high)//2
        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar :
            low = mid+1
        else:
            end = mid-1
    return -1



array=[2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
target=72
result=binarySearch(array, target)
if result == -1 :
    print('Element Not Found')
else:
    print('Element Found At Index ',result)