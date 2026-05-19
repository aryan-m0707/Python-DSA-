# #Selection Sort
def selectionSort(array):
    for i in range(len(array)):
        min=i
        j=i+1
        while j<len(array):
            if array[j]<array[min]:
                min=j
            j+=1 
            array[i],array[min]=array[min],array[i]
        print(array)
array=[20,12,10,15,2]
print("Original Array:",array)
selectionSort(array)