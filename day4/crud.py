import sys
class StudentInfo:
    def __init__(self):
        print('Student Managemant System.')
    
    def addStudentInfo(self):
        id=int(input('Enter Stdent ID: '))
        rollNo=int(input('Enter Stdent Roll No: '))
        name=input('Enter Stdent Name: ')
        city=input('Enter Stdent City: ')
        

    def showStudentInfo(self):
        pass

    def updateStudentInfo(self,id):
        pass

    def deleteStudentInfo(self,id):
        pass

stdObj = StudentInfo()

while True:
    print('1. Add Student')
    print('2. Show Student')
    print('3. Update Student')
    print('4. Delete Student')
    print('5. Exit')
    choice = int(input('Select any choice: '))
    if choice == 1:
        stdObj.addStudentInfo()
    elif choice == 2:
        stdObj.showStudentInfo()
    elif choice == 3:
        stdObj.updateStudentInfo()
    elif choice == 4:
        stdObj.deleteStudentInfo()
    else:
        sys.exit()
    