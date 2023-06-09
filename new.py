# class Student:
#     name='Neeraj'
#     @classmethod
#     def stu_datails(cls):
#         return cls.name
# print("Result:",Student.stu_datails())
class Student:
    name='Neeraj'
    @staticmethod
    def stu_datails():
        return Student.name
print("Result:",Student.stu_datails())