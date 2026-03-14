class Student:
    def __init__(self,full_name,age,adres):
        self.full_name=full_name
        self.age=age
        self.adres=adres

    def get_info(self):
        return f"""{self.full_name.title()}, ({self.age} yosh) yashash joyi: {self.adres.title()}"""

student1=Student('Ali',17,'Chorsu')
student2=Student('Vali',14,'Yakkasaroy')
student3=Student('Olim',19,'Chorsu')
student4=Student('Davron',25,'Chorsu')

class Group:
    def __init__(self,title):
        self.title=title
        self.students=[]

    def add_student(self,*args):
        for x in args:
            if isinstance(x,Student):
                self.students.append(x)
            else:
                print("Mavjud emas!")

    def get_all_info(self):
        length = len(self.students)
        maximum = max([x.age for x in self.students])
        data1 = [x.get_info() for x in self.students if x.age == maximum]
        minimum = min([x.age for x in self.students])
        data2 = [x.get_info() for x in self.students if x.age == minimum]
        return f"""
Studentlar soni: {length} nafar
Eng yoshi kattasi: {data1[0]}
Eng yoshi kichigi: {data2[0]}
"""



front=Group('Frontend')
front.add_student(student1,student2)
back=Group('Backend')
back.add_student(student3,student4)
print(back.get_all_info())