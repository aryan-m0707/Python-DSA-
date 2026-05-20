# # input='leetcode'
# # # output='l'
# # count=1
# # for i in range(len(input)-1):
# #     if input[i] in input[i+1:len(input)]:
# #         continue
# #     else:
# #         if count == 1:
# #             print(input[i])
# #             break
# #         count+=1
 

# # n=int(input('Enter number of element: '))
# # myList=[]
# # for i in range(n):
# #     =map(int,input())



# input=[7,9,-3,8,-6,7,8,10]
# max=0
# sum=0
# for i in range(len(input)-1):
#     for j in range(i+1,len(input)):
#         if max < input[i]*input[j]:
#             max=input[i]*input[j]
#             sum=input[i]+input[j]
# print(sum)


input= [1,2,3,4,5]
# output=[4,5,1,2,3]
k=2
n=len(input)
start=input[n-k:] + input[:k+1]

print(start)