class Collage:
    def collagename(self):
        print('Modern Collage')
    
class Student(Collage):
    def student_info(self):
        print('Name: Prashant Jha')
        print('Branch: Mechanical')
    
obj=Student()
obj.collagename()
obj.student_info()