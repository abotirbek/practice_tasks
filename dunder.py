# class Car:
#     def __init__(self,title):
#         print('init',self)
#         self.title=title
#
#     def __new__(cls, *args, **kwargs):
#         print('new',cls,args,kwargs)
#         if args[0]=='monza':
#             print('Mumkin emas')
#         else:
#             return super().__new__(cls)
# new = Car('monza')
# new1 = Car('monzas')

# class Car:
#     def __init__(self,title, price):
#         print('init',self)
#         self.title=title
#         self.price = price
#
#     def __setattr__(self, key, value):
#         print('setattr',key,value)
#         return super().__setattr__(key,value)
#
# obj = Car('monza',20000)
# print(obj)

# Phone
# brand,price
# agar man unda obj.color bunday xususiyat yoq
# agar price ozgartirmoqchi bolsam nech marta ozgarish qilganimni aytsin

# class Phone:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#         self.change_brand = 0
#
#     def __setattr__(self, key, value):
#         if key == 'brand' and self.brand != value:
#             self.update_change()
#
#     def update_change(self):
#         self.change_brand += 1
#
#
#     def __getattr__(self, item):
#         return f"\"{item}\" atributi mavjud emas"
#
#     def __getattribute__(self, item):
#         return super().__getattribute__(item)
#
#     def get_info(self):
#         return f"{self.brand} --- {self.price}"
#
# phone1 = Phone('iPhone 17',1500)
# phone1.brand = 'iPhone 17 max'
# print(phone1.__dict__)
# print(phone1.get_info())

