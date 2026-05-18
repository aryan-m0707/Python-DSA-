# # consicutive 1's
# input=[1,1,0,1,1,1,0,1,1,1,1,1,0,0,1]
# ans=0
# count=0 
# for i in input:
#     if i == 1:
#         count+=1
#     else:
#         if count >ans:
#             ans=count
#             count=0

# if count>ans:
#     print(count)
# else:
#     print(ans)


# input="abababab"
# target="ab"
# # print(input.count("ab"))
# ans=0
# for i in range(0,len(input),2):
#     # print(i)
#     if (input[i]+input[i+1])==target:
#         ans+=1
# print(ans)


# m=[[100,198,333,323],
#  [122,232,221,111],
#  [223,565,245,764]]
# newList=[]
# for i in range(len(m)):
#     max=m[i][0]
#     for j in range(len(m[i])):
#         if max < m[i][j]:
#             max=m[i][j]
#     newList.append(max)
# print(newList)


input="prashant*is*a*good*programmer"
# star=input.count("*")
# string1=input.replace("*","")
# for i in range(star):
#     string1="*"+string1
# print(string1)



input="aaabbbbccceeeee"
# output="a3b4c3e5"
dic={}
for ele in input:
    if ele not in dic:
        dic[ele]=0
    dic[ele]+=1
print(dic)
# ans=""
# for ele in dic:
#     ans+=ele+str(dic[ele] )
# print(ans)
for i,j in dic.items():
    print(i,j,sep="",end="")