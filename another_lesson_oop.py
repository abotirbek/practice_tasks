# class Car:
#     def __init__(self):
#         pass
#
#     @classmethod
#     def verify_num(cls,x):
#         if x%2==0:
#             print(f"{x} --- juft")
#         else:
#             print(f"{x} --- toq")
#
#     def get_info(self):
#         return "Bu ma'lumot objectniki"
#
#     @staticmethod
#     def add_nums(x,y):
#         return x+y
#
# print(Car.verify_num(12))
# obj = Car()
# print(Car.get_info(obj))


# class Bezon:
#     filial = []
#
#     def __init__(self,count,price,location):
#         self.count = count
#         self.price = price
#         self.location = location
#         Bezon.filial.append(self)
#
#     def find_len(self):
#         return f"Filiallar soni: {len(self.filial)}"
#
#     def check_comp_count(self,x,y):
#         if self.count >= x:
#             print(f"{self.count}ta kompyuter bo'sh")
#             total_price = y * self.price * x
#             per_person = self.price * y
#             print(f"Jami narx: {total_price} so'm\nKishi boshiga: {per_person}")
#         else:
#             print(f"{x-self.count}ta kam kompyuter")
# chorsu = Bezon(20,50000,'Chorsu')
# yunus = Bezon(40,40000,'Yunusobod')
# dustlik = Bezon(30,45000,"Do'stlik")
# mir_ul = Bezon(15,30000,"Mirzo Ulug'bek")
# print(yunus.find_len())
# print(chorsu.check_comp_count(15,4))




# class BankAccount:
#     items = []
#
#     def __init__(self,username,balance):
#         self.username = username
#         self.balance = balance
#         BankAccount.items.append(self)

    # def add_money(self,new):
    #     if new < 1000:
    #         self.balance += new
    #         return f"Yangi balans: {self.balance}"
    #     else:
    #         return f"Limit 1000gacha"
    #
    # def spend_money(self,old):
    #     if old > self.balance:
    #         return f"Balansda {old} summa yo'q"
    #     else:
    #         used = self.balance-old
    #         return f"Qoldi: {used}"
    #
    # def get_balance(self):
    #     return f"Jami summa: {self.balance}"

    # def transaction(self,search,amount):
    #     for i in self.items:
    #         if i.username == search:
    #             i.balance += amount
    #             self.balance -= amount
    #             print(f"Sizdagi summa: {self.balance}, {i.username}dagi summa: {i.balance}")
    #             break
    #         else:
    #             print(False)




# obj1 = BankAccount('Zakariyo',400)
# obj2 = BankAccount('Azamat',600)
# # print(obj1.add_money(900))
# # print(obj1.spend_money(1000))
# print(obj1.transaction('Azamat',100))



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# person1 = Person('Ali',25)
# print(hasattr(person1,'name'))
# print(hasattr(person1,'salary'))
# print(getattr(person1,'name'))
# print(getattr(person1,'salary','Not Available'))
# setattr(person1,'age',30)
# print(person1.age)
# setattr(person1,'salary',5000)
# print(person1.salary)
# delattr(person1,'age')
# print(hasattr(person1,'age'))

# class Car:
#     def __init__(self,title,price):
#         self.title = title
#         self.price = price
#
#     def get_info(self):
#         if hasattr(self,'title'):
#             return f"{self.title} narxi esa {self.price}"
#         else:
#             self.title = 'Noma\'lum'
#             return f"{self.title} narxi esa {self.price}"
# obj = Car('Tico',2000)
# obj2 = Car('Matiz',3000)
# del obj.title
# print(obj2.get_info())
# print(obj.get_info())


# # 1-masala
# class Person:
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name
#
#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.age}"
#
#     @classmethod
#     def from_birth_years(cls,name,birth_year):
#         return cls(name, 2026-birth_year)
#
# p1 = Person.from_birth_years('Ali',2006)
# print(p1.get_info())

# #2
# class Student:
#     def __init__(self,fullname,grade):
#         self.fullname = fullname
#         self.grade = grade
#
#     def get_info(self):
#         return f"{self.fullname.capitalize()} --- {self.grade}-sinf"
#
#     @staticmethod
#     def validate_grade(grade):
#         if 1<=grade<=11:
#             return True
#         else:
#             return False
#
#     @classmethod
#     def create_if_valid(cls, fullname, grade):
#         if grade:
#             return cls(fullname,grade)
#         else:
#             raise ValueError("Invalid grade")
# s1 = Student.create_if_valid('azizbek',9)
# print(s1.get_info())

#3
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.brand.capitalize()} {self.model.capitalize()} ({self.year})"

    @staticmethod
    def is_old(year):
        return year < 2016

    @classmethod
    def from_string(cls,car_string):
        items = car_string.split(',')
        news = []
        for i in items:
            i = i.strip()
            news.append(i)
        if int(news[-1]):
            return cls(news[0],news[1],int(news[2]))
        else:
            raise ValueError('Invalid Year')
car1 = Car.from_string("Toyota, Camry, 2015")
print(car1.get_info())
print(Car.is_old(car1.year))