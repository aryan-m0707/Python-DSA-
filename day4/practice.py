# salary=int(input('Enter your salary : '))
# rating=int(input('Enter your performance appraisal rating : '))
# increment=0
# if rating >= 1 and rating <= 3:
#     increment=salary*10/100
# elif rating >= 3.1 and rating <= 4:
#     increment=salary*20/100
# elif rating >= 4.1 and rating <= 5:
#     increment=salary*40/100
# else:
#     print('Invalid rating')
# print('Increment Salary: ',increment+salary)


# basicSalary=20000
# # so we have to calaculate the 
# # HRA of basicSalary = 20%
# # TA of basicSalary = 30%
# # DA of basicSalary = 45%
# # calculate GrossSalary = ?
# HRA=basicSalary*0.2
# TA=basicSalary*0.3
# DA=basicSalary*0.45
# print(basicSalary+HRA+TA+DA)


# input=[5,7,8,3,7,8,9,2,3]
# dic={}
# for ele in input:
#     if ele not in dic:
#         dic[ele]=0
#     dic[ele]+=1
# print(dic)
# mylist=[]
# for ele in dic:
#     if dic[ele]>1 :
#         mylist.append(ele)
# print(len(mylist))


input=[5,7,2,3,7,8,2,3,3]
target=3
count=0
for ele in input:
    if target == ele:
        count+=1
print(count)