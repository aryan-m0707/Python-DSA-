import csv
f=open('StudentData.csv','a')
a=csv.writer(f)
studId=int(input('Enter Student Id: '))
studName=input('Enter Student Name: ')
phy=int(input('Enter Physics Marks: '))
chem=int(input('Enter chemistery marks: '))
math=int(input('Enter math marks: '))
Total=phy+chem+math
per=(Total/300)*100
a.writerow([studId,studName,phy,chem,math,Total,per])
