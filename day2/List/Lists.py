# myList = ["prashant","Ashish","komal","ankush","ashish",77,"sandip",60.52,"prashant"]

# print(myList)   #   ['prashant', 'Ashish', 'komal', 'ankhush', 'ashish', 77, 'sandip', 60.52, 'prashant']
# print(type(myList)) #   <class 'list'>
# print(myList[0])    #   prashant
# print(myList[1])    #   Ashish
# print(myList[2])    #   komal
# print(myList[-1])   #   prashant
# print(myList[2:5])  #   ['komal', 'ankhush', 'ashish']
# print(myList[:5])   #   ['prashant', 'Ashish', 'komal', 'ankhush', 'ashish']
# print(myList[1:])   #   ['Ashish', 'komal', 'ankhush', 'ashish', 77, 'sandip', 60.52, 'prashant']
# print(myList[1:8:2])    #   1,3,5,7 ['Ashish', 'ankhush', 77, 60.52]


# myList[2]="Akshay"
# print(myList)   #   ['prashant', 'Ashish', 'Akshay', 'ankhush', 'ashish', 77, 'sandip', 60.52, 'prashant']

# if "ankush" in myList:
#     print("Yes ankush is available")
# else:
#     print('not allowed')

# myList.append('harsh')
# myList.append('laxman')
# print(myList)   #   ['prashant', 'Ashish', 'Akshay', 'ankhush', 'ashish', 77, 'sandip', 60.52, 'prashant', 'harsh', 'laxman']

# myList.insert(3,'sandip')
# print(myList)

# myList.remove('sandip')
# print(myList)

# newList=myList.copy()
# print(newList)


# myList=[['prashant','jha'],["85.56"],[44002,"yyy"]]

# print(myList)   #   [['prashant', 'jha'], ['85.56'], [44002, 'yyy']]
# # print(myList[row][col])   
# print(myList[0][0]) #   prashant
# print(myList[0][1]) #   jha
# print(myList[1][0]) #   85.56
# print(myList[2][0]) #   44002
# print(myList[2][1]) #   yyy


# list2=[50,25.50,'prashant']
# del list2[2]
# del list2
# print(list2)

# list2=[50,25.50,'prashant']
# list2.clear()
# print(list2)

# name="prashant"
# print(name)#prashant
# myname=list(name) # first split then add to list
# print(myname)#['p', 'r', 'a', 's', 'h', 'a', 'n', 't']


# myList=[44,22,77,0,9,88]
# myList.sort()
# print(myList)   #[0, 9, 22, 44, 77, 88]
# myList.sort(reverse=True)
# print(myList)   #[88, 77, 44, 22, 9, 0]

# myList=[44,22,77,0,9,88]
# newlist=myList
# print(id(myList))
# print(id(newlist))

