
'''
class New:

    def __init__(self):
        self.name = "Prashant"

obj1 = New()
obj2 = New()
obj3 = New()

'''


# For every object a separate copy of instance variable created,
# but in case of static variable only one copy will be created
# and it is accessible for every object of the class.

class College:

    collegename = "Modern College"   # static variable (1 memory)

    def __init__(self):
        self.studentname = "prashant"   # instance variable (separate memory)


principal = College()   # object creation
teacher = College()
accountant = College()

print("principal:", principal.collegename, ":", principal.studentname)
print("teacher :", teacher.collegename, ":", teacher.studentname)
print("accountant:", accountant.collegename, ":", accountant.studentname)

College.collegename = "JIO"   # changing static variable

principal.studentname = "prashant jha"

print("principal:", principal.collegename, ":", principal.studentname)
print("teacher :", teacher.collegename, ":", teacher.studentname)
print("accountant:", accountant.collegename, ":", accountant.studentname)