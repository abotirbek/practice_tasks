# #1
# class User:
#     def __init__(self,name):
#         self.name = name
#
#     def __getattr__(self, item):
#         return f"\"{item}\" atributi mavjud emas"
# u = User('Ali')
# print(u.phone)

# #2
# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#
#     def __getattr__(self, item):
#         return None
# p = Product('Cola',12000)
# print(p.stock)

# #3
# class Book:
#     def __init__(self,title,price):
#         self.title = title
#         self.price = price
#
#     def __getattribute__(self, item):
#         return f"{item} atributi o'qildi"
# b = Book('Python',50000)
# print(b.title)

# #4
# class User:
#     def __setattr__(self, key, value):
#         if value:
#             print(f"{key} atributiga qiymat berildi")
#         else:
#             print(None)
# x = User()
# x.name = 'Ali'


# #5
# class Product:
#     def __setattr__(self, key, value):
#         if key == 'price':
#             if value < 0:
#                 print('Xato: price manfiy bo\'lishi mumkin emas')
#             else:
#                 return super().__setattr__(key,value)
# p = Product()
# p.price=500

# #6
# class User:
#     def __new__(cls, *args, **kwargs):
#         if not args is None:
#             print("User object yaratilmoqda")
#             return super().__new__(cls)
# u = User()

# #6
# class User:
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not args is None:
#             print(args)
#             print("User object yaratilmoqda")
#             return super().__new__(cls)
# u = User()
# u.name = 'ali'

9️⃣ __setattr__ — atributni bloklash

Class: User

class User:
    pass

Vazifa

id atributi faqat bir marta berilishi mumkin.

Agar ikkinchi marta berilsa:

id ni o'zgartirish mumkin emas

chiqsin.

Tekshirish

u = User()
u.id = 10
u.id = 20


