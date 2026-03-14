#1
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def update_grade(self):
        new_grade = int(input("Yangi ball (0-100): "))
        while not 0<=new_grade<=100:
            new_grade = int(input("Yangi ball (0-100): "))
        return new_grade


    def get_info(self):
        new = self.update_grade()
        if self.age<7:
            self.age = f'Faqat 7dan katta'
        if not 0<=self.grade<=100:
            self.grade = new
        return f"""
{self.name.upper()} ({self.age} yosh) — {self.grade} ball
"""

student1 = Student('Ali',5,101)
print(student1.get_info())
