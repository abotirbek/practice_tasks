# class Car:
#     def __init__(self,brand,price,id):
#         self.brand = brand
#         self.price = price
#         self.__id = id
#
#     def get_id(self):
#
#         return self.__id
#
#     def update_id(self,id):
#         if type(id) != str or len(id) < 6 or ' ' in id:
#             return 'Xato'
#         else:
#             self.__id =id
#             return 'ID yangilandi'
#
#     @property
#     def id(self):
#         return self.__id
#
#     @id.setter
#     def id(self,id):
#         if type(id) != str or len(id) < 6 or ' ' in id:
#             print('Xato')
#         else:
#             self.__id =id
#             print('ID yangilandi')
#
# new = Car('Onix',1400,'ac12321')
# # new.id = 'nima1234865'
# # print(new.update_id('salome'))
# new.id = 'ss'
# print(new.id)


class Employee:
    HARF = 'qwertyuiopasdfghjklzxcvbnm'
    KATTA_HARF = HARF.upper()

    def __init__(self,fio,age,weight,ps):
        self.verify_fio(fio)
        self.verify_weight(weight)
        self.__fio = fio
        self.__age=age
        self.__weight = weight
        self.__ps=ps

    @classmethod
    def verify_fio(cls,new):
        if type(new) != str:
            raise TypeError('Faqat string')
        fio_list = new.split()
        if len(fio_list)!=3:
            raise ValueError('Faqat FISH')
        standard = cls.HARF + cls.KATTA_HARF
        for text in fio_list:
            for h in text:
                if not h in standard:
                    raise ValueError('FISH faqat lotin harflarda')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self,new):
        self.verify_fio(new)
        self.__fio=new

    def verify_age(self, new_age):
        if type(new_age) != int:
            raise TypeError('Faqat sonlar')
        if not 18 < new_age < 120:
            raise ValueError('Faqat 18-120')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new):
        self.verify_age(new)
        self.__age=new

    @classmethod
    def verify_weight(cls,new):
        if not type(new) in (int, float):
            raise TypeError('Faqat integer yoki Float')
        if not 45<new<200:
            raise ValueError('Faqat 45-200')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,new):
        self.verify_weight(new)
        self.__weight=new

    @classmethod
    def verify_id(cls,new):
        if type(new) != str:
            raise TypeError('Faqat \"AA 1234567\" ko\'rinishida')
        two_parts = new.split()
        if len(two_parts) != 2:
            raise ValueError('Faqat \"AA 1234567\" ko\'rinishida')
        if len(two_parts[0]) != 2:
            raise ValueError('Faqat \"AA 1234567\" ko\'rinishida')
        if not two_parts[0].isalpha():
            raise TypeError('Faqat \"AA 1234567\" ko\'rinishida')
        if not two_parts[-1].isdigit():
            raise TypeError('Faqat \"AA 1234567\" ko\'rinishida')
        if len(two_parts[-1]) != 7:
            raise ValueError('Faqat \"AA 1234567\" ko\'rinishida')

    @property
    def id(self):
        return self.__ps

    @id.setter
    def id(self, new):
        self.verify_id(new)
        self.__ps = new


obj = Employee('Ali Valiyev Sobir', 20, 90, 'ab1234567')
# obj.fio = 'vali ali nima52154'
# print(obj.fio)
# obj.age = '26'
# print(obj.age)
# print(obj.verify_age(19))
# obj.weight = 100
# print(obj.weight)

obj.ps = 'AA 1234567'
print(obj.ps)