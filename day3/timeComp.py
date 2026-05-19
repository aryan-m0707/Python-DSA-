# find the Maximum number in an array
def findBiggestNumber(nums):
    Maximum=nums[0]    #O(1)
    for i in range(1, len(nums)):    #O(N)
        if nums[i]> Maximum:   #O(1)
            Maximum=nums[i] #O(1)
    print(Maximum)   #O(1)
        
nums=[5,7,9,2,3,4,]#O(1)
findBiggestNumber(nums)#O(1)