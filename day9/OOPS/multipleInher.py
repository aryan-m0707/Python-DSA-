# class SubjMarks:
#     math = int(input('Enter paper marks of math :'))
#     DE = int(input('Enter paper marks of designe engineering :'))
#     c = int(input('Enter paper marks of c language :'))
#     english = int(input('Enter paper marks of english :'))

# class PractMarks:
#     cpract = int(input('Enter practicals marks of c language :'))

# class Result(SubjMarks,PractMarks):
#     def total(self):
#         if self.math >= 40 and self.DE >= 40 and self.c >= 40 and self.english >= 40 and self.cpract >= 40 :
#             print('Pass')
#         else:
#             print('Fail')

# obj = Result()
# obj.total()


class A:
    def add(self):
        print('class A')

class B:
    def add(self):
        print('class B')

class C(A,B):
    def add(self):
        print('class C')

obj=C()
obj.add()