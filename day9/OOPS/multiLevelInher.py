class Collage:
    def collagename(self):
        print('Modern Collage')
    
class Student(Collage):
    def student_info(self):
        print('Name: Prashant Jha')
        print('Branch: Mechanical')
    
class Exam(Student):
    def subject(self):
        print('Subject1: Designe Engineering')
        print('Subject2: Math')
        print('Subject3: C-Language')


obj=Exam()
obj.collagename()
obj.student_info()
obj.subject()