# class Weather:
#     def __init__(self,temp,location):
#         self.daraja = temp
#         self.address = location
#
#     def __repr__(self):
#         return f"{self.address}da bugun havo {self.daraja}"
#
#     def __str__(self):
#         return self.address
#
# obj = Weather('-4C','Toshkent')
# obj2 = Weather('-4C','Andijon')
# print(repr(obj))
# print(obj2)

# class Product:
#     def __init__(self,title,price,quantity):
#         self.title=title
#         self.price=price
#         self.quantity=quantity
#
#     def __len__(self):
#         total = self.price * self.quantity
#         return total
#
# obj = Product('redmi',200,50)
# print(len(obj))

class Time:
    DAY = 86400

    def __init__(self,second):
        self.second = second

    def get_time(self):
        s=self.second%60
        m=(self.second//60)%60
        h=(self.second//3600)%24
        return f"{self.get_formated(h)}:{self.get_formated(m)}:{self.get_formated(s)}"

    @classmethod
    def get_formated(cls,x):
        return str(x).rjust(2,'0')

    def __add__(self, x):
        if isinstance(x,Time):
            return Time(self.second+x.second)
        elif isinstance(x,int):
            return Time(self.second+x)
        else:
            raise TypeError("Xato Qiymat")

    def __sub__(self, x):
        if isinstance(x,(Time,int)):
            if isinstance(x,Time):
                result = x.second
            else:
                result = x
        else:
            raise ValueError("Xato Qiymat")
        return Time(self.second-result)

#     def __mul__(self, x):
#         if isinstance(x, (Time, int)):
#             if isinstance(x, Time):
#                 result = x.second
#             else:
#                 result = x
#         else:
#             raise ValueError("Xato Qiymat")
#         return Time(self.second * result)
#
#     def __truediv__(self, x):
#         if isinstance(x,(Time,int)):
#             if isinstance(x,Time):
#                 result = x.second
#             else:
#                 result = x
#         else:
#             raise ValueError("Xato Qiymat")
#         return Time(self.second/result)
#
# obj = Time(72)
# obj2 = Time(62)
# obj /= obj2
# print(obj.get_time())

# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
#     def __eq__(self, other):
#         return self.grade == other.grade
#     def __ne__(self, other):
#         return self.grade != other.grade
#     def __lt__(self, other):
#         return self.grade < other.grade
#     def __le__(self, other):
#         return self.grade <= other.grade
#     def __gt__(self, other):
#         return self.grade > other.grade
#     def __ge__(self, other):
#         return self.grade >= other.grade
# s1 = Student('Ali',85)
# s2 = Student('Vali',90)
# print(s1 == s2)
# print(s1 != s2)
# print(s1 < s2)
# print(s1 <= s2)
# print(s1 > s2)
# print(s1 >= s2)

# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
#     def __eq__(self, other):
#         return self.grade == other.grade and self.name == other.name
#     def __hash__(self):
#         return hash((self.name,self.grade))
# obj1 = Student('Ali',90)
# obj2 = Student('Ali',90)
# new_dict = {
#     'apple':'olma',
#     'name':'ali',
#     'name':'vali',
#     obj1:'salom',
#     obj2:'xayr'
# }
# print(new_dict)
# print(obj1==obj2)
# print(obj1 is obj2)

class Group:
    def __init__(self, title, time_start, days, *args,**kwargs):
        self.title = title
        self.time_start = time_start
        self.days = days
        self.members = list(args)
        self.room = kwargs

    def __getitem__(self, item):
        if type(item)==int:
            return self.members[item]
        elif type(item)==str:
            return self.room.get(item,'Not Available')

    def __setitem__(self, key, value):
        if type(key)==int:
            self.members[key]=value
        elif type(key)==str:
            self.room[key]=value

    def __str__(self):
        return self.title

kunlar = ['Du','Chor','Ju']
new=Group('u17',"16:30",kunlar,'zakariyo','botirjon','azamat','isfandiyor','bahromjon','anvarjon',stul=7,window='big',svet='light')
# print(new[20])
print(new['stul'])