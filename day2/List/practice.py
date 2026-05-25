# list=[0,1,4,0,2,5]
# con=0
# for i in list:
#     if i==0:
#         list.remove(i)
#         list.append(i)
# print(list)


# list=[7,3,9,2,8] #8
# list.sort()
# print(list[-2])


# a=[1,2,3,4,5,6,7,8,9]
# # a[start:end:iteration]
# a[::2]=10,20,30,40,50,60    # iterate every time by 2 and assing the value
# print(a)


# a=[1,2,3,4,5]
# print(a[3:0:-1])
# A. Syntax error
# B. [4,3,2]
# C. [4,3]
# D. [4,3,2,1


# arr=[[1,2,3,4],
#      [4,5,6,7],
#      [8,9,10,11],
#      [12,13,14,15]]

# for i in range(0,4):
#     print(arr[i].pop())

# A. 1 4 8 12
# B. 2 3 4 1
# C. 4 7 11 15
# D. 3 5 7 4



# fruit_list1 = ['Apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum=0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#         sum+=1
#     if ls[1] == 'Kiwi':
#         sum+=20
# print(sum)



# list1=[1,2,3]
# list2=[2,3,4]
# list3=[3,4,5]

# for i in list1:
#     if i in list1 and i in list3:
#         print(i)

list=[]
for i in range(5):
    list.append(int(input("Enter any value: ")))

print(list)
sum=0
for i in range(1,5):
    sum+= abs(list[i]-list[i-1])

print(sum) 