# input="Hello world"
# mylist=input.split(" ")
# # print(mylist)
# ans=""
# for ele in mylist:
#     rev=""
#     for i in ele:
#         rev=i+rev
#     ans+=rev+" "
# print(ans)


# input="({{()}})"
# # output=valid
# ans=0
# myList=[]
# for i in input:
#     if i=='(' or i=='{' or i=='[':
#         myList.append(i)
#     elif i==')': 
#         if '(' in myList:
#             myList.remove('(')
#         else:
#             myList.append(i)
#     elif i=='}': 
#         if '{' in myList:
#             myList.remove('{')
#         else:
#             myList.append(i)
#     elif i==']': 
#         if '[' in myList:
#             myList.remove('[')
#         else:
#             myList.append(i)
#     else:
#         print('Invalid')
    
# if myList==[]:
#     print('Valid')
# else:
#     print('Invalid')


# myList=[4,3,2,7,8,2,1,5,5]
# dic={}
# for ele in myList:
#     if ele not in dic:
#         dic[ele]=0
#     dic[ele]+=1
# # print(dic)
# for ele in dic:
#     if dic[ele] > 1:
#         print(ele,end=" ")


# ----------------------------------------------------------------
# dic={'C':3,'B':2,'A':1}
# asc={}
# while dic !={}:
#     if dic[i]
# ----------------------------------------------------------------

class College:
    collegename="Modern College"  # static variable

    def __init__(self):
            self.studentname="Prashant"

principal=College()
teacher=College()
accountant=College()

print("principal= " ,principal.collegename, ".........", principal.studentname)
print("teacher= ", teacher.collegename, ".......", teacher.studentname)
print("accountant= ", accountant.collegename, ".........", accountant.studentname)
College.collegename='HBD'
principal.studentname="Prashant jha"
print("principal= " ,principal.collegename, ".........", principal.studentname)
print("teacher= ", teacher.collegename, ".......", teacher.studentname)
print("accountant= ", accountant.collegename, ".........", accountant.studentname)
