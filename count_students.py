class Student:
    __student_count = 0
    def __init__(self,name,age):
        self.is_adult(age)
        self.name = name
        self.age = age
        Student.__student_count += 1

    @classmethod
    def is_adult(cls,new):
        return new >= 18

    @classmethod
    def get_students_count(cls):
        return cls.__student_count

s1 = Student('Ali',19)
s2 = Student('Bobur', 17)
print(Student.get_students_count())
print(Student.is_adult(19))          # True
print(Student.is_adult(17))    