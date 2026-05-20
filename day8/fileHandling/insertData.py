import csv

f=open('employee.csv','a')
a = csv.writer(f)
# a.writerow(['Emp ID','Emp Name','Emp Age'])  
empId=int(input('Enter your EmpId: '))
empName=input('Enter Employee Name: ')
empAge=int(input('Enter Employee Age: '))
a.writerow([empId,empName,empAge])
print('File has created')