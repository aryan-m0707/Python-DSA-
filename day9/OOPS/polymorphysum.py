# class rbi:
#     def home_loan(self):
#         print('Home Loan ROI = 8%')

#     def education_loan(self):
#         print('Educaton Loan ROI = 9%')

# class sbi(rbi):
#     def education_loan(self):
#         print('Educaton Loan ROI = 10%')
#     super().education_loan()

# obj=sbi()
# obj.education_loan()


class rbi:
    def __init__(self):
        print('Parent class contructor')

class sbi(rbi):
    def __init__(self):
        print('Child class contructor')
        super()

obj=sbi()