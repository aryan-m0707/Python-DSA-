# myList=[0,0,1,2,0,3,0,0,4]
# i=0
# while myList[i] == 0:
#     myList.remove(0)
# print(myList)


myList=[3,4,-1,1]
for i in range(1,len(myList)):
    if i not in myList:
        print(i)
        break
