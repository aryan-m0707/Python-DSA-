# #Insertion Sort
def insertionSort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
        print(array)
        print()
array=[5,3,6,8,2]
print("Original Array:",array)
insertionSort(array)