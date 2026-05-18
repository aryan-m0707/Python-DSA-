# n=int(input('Enter the size of Array: '))
# nums=[]

# for i in range(n):
#     nums.append(int(input('Enter Array element: ')))
# # print(nums)

# nums=[79,77,34,81,48,34,25,16]
# ans = 0 
# for ele in nums:
#     i=1
#     while (i*i) <= ele:
#         if i*i == ele:
#             ans+=1
#             break
#         i+=1
# print(ans)
        

# def func(value,values):
#     var=1
#     values[0]=44

# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0])
# options
# A. 1 44
# B. 3 1
# C. 3 44
# D. 1 3


# def f(i,values=[]):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)
# Options
# A. [1] [2] [3]
# B. [1, 2, 3]
# C. [1] [1, 2] [1, 2, 3]
# D. 1 2 3


# fruit={}
# def addone(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))
# print(fruit)
# Options
# A. 1
# B. 2
# C. 3
# D. 4


# Write a program to accept student name and marks from a keyboard
# and create a dictionary. Also display student markes by taking student name
# n=int(input('Enter the number of Students: '))
# std={}
# for i in range(n):
#     name=input('Enter Student Name: ')
#     mark=int(input('Enter Student Marks: '))
# while True:
#     name=input('Enter Student Name to get Marks: ')
#     mark=std.get(name,-1)
#     if mark == -1:
#         print('Student not found')
#     else:
#         print('The Marks of {} are {}',name,mark)
#     option=input('Do you want to find another student marks [Yes/No].')
#     if option == 'No':
#         break
# print('Thanks for using our application')


# Write a program to access each charactor to string in forward and 
# backward direction by using while loop?
# input='Learning Python is very easy'
# i=0
# while i<len(input):
#     print(input[i],end=' ')
#     i+=1
# print()
# print('Backword Direction')

# j=-1
# while j>=-len(input):
#     print(input[j],end=' ')
#     j-=1

# ----------------------------------------------------
# str='abcdfjgerj abcdfjger'
# lis=str.split(' ')
# str1=str[0]
# str2=str[1]
# l=len(str1)
# m=len(str2)
# i=0
# while l>=m:
#     if str1[i] != str2[i]:
#         print(str1[i])
#         i+=1
# if i != l-1:
#     print(str1)
# -----------------------------------------------------


# v=['a', 'e', 'i', 'o', 'u']
# w=input('Enter the word where we will search the vowels: ')
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels=',found)
# print('Unique vowels',len(found),'from the give word =',w)



# x,y,z=map(int,input().split())
# myList=[29,38,12,48,39,55]
# for ele in myList:
#     if  ele >= y and ele <= z :
#         print(ele,end=' ')


# import datetime
# date=datetime.datetime.now()
# print('It\'s now: {:%d/%m/%Y %H:%M:%S}'.format(date))


# val=[2**i for i in range(1,6)]
# print(val)#[2, 4, 8, 16, 32]


# val=[i*i for i in range(1,11)]
# print(val)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# squares={x:x*x for x in range(1,6)}
# print(squares)


# doubles={x:2*x for x in range(1,6)}
# print(doubles)


# a,b=[int(x) for x in input('Enter 2 numbers: ').split()]
# print('Product is :',a*b)


# a,b,c=[float(x) for x in input('Enter 3 float numbers :').split()]
# print('The Sum is :',a+b+c)


# myCard=[10,20,800,60,70]
# for item in myCard:
#     if item > 400:
#         print('This is not in my budget')
#         continue
#     print(item)
# else:
#     print('You have purchased everything.')


username='admin'
password='admin'

while True:
    name=input('Enter user name: ')
    passw=input('Enter user password: ')
    if name==username and passw==password :
        print('login successfully')
        break
