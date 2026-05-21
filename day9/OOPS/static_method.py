class Student:
    @staticmethod
    def get_personal_detail(firstname,lastname):
        print('your personal detail=',firstname,lastname)
    @staticmethod
    def contact_detail(mobile_no,rollno):
        print('your contact detail=',mobile_no,rollno)

Student.get_personal_detail('Himanshu','jha')
Student.contact_detail(8456975462,1001)