#8
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def increase_salary(self,percent):
        if 0<percent<=30:
            self.salary *= (percent+100)/100
        else:
            pass

    def get_info(self):
        self.increase_salary(20)
        if self.salary < 1000000:
            self.salary = 'Xato!'
        return f"""
{self.name.capitalize()}ning oyligi {self.salary} so'm"""

employee1 = Employee('Ali',1000000)
print(employee1.get_info())