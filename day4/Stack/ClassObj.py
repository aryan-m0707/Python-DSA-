# class Name:
#     age=30
#     def display(self):
#         print('Hello world')

# obj = Name()
# print(obj.age)
# obj.display()


# class Student:
#     def __init__(self):
#         self.name='Prashant'
#         self.age=30

#     def display(self):
#         print('Name = ',self.name)
#         print('Age = ',self.age)

# obj= Student()
# print(obj)


#constructor
# class Message:
#     def __init__(self):#contructor
#         print('I am a contructor')

#     def display(self):
#        print('class program')

# obj= Message()
# obj.display()
# obj= Message()


# Types of contructor
#parameterize constructor
class StudentInfo:
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no
    
    def displayStudentInfo(self):
        print('Name = ',self.name)
        print('Age = ',self.age)
        print('Roll no. = ',self.roll_no)

stdObj=StudentInfo('Himanshu',34,101)
stdObj.displayStudentInfo()