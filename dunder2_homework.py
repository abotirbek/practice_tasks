#1
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        return Vector(self.a + other.a,self.b + other.b)

    def __str__(self):
        return f"Vector({self.a},{self.b})"
v1 = Vector(2,3)
v2 = Vector(4,5)
print(v1+v2)

#2
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def __sub__(self, other):
        return BankAccount(self.name, self.balance - other.balance)
    def __str__(self):
        return f"{self.balance}"
a1 = BankAccount("Ali", 1000)
a2 = BankAccount("Vali", 600)
print(a1-a2)

#3
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __mul__(self, other):
        return self.price * other
    def __str__(self):
        return f"{self.price}"
p = Product('Olma',5000)
print(p*3)

#4
class Student:
    def __init__(self,name,total_score,subject_count):
        self.name = name
        self.score = total_score
        self.sub_num = subject_count
    def __truediv__(self, other):
        return int(self.score/self.sub_num)
    def __str__(self):
        return f"{self.score}"
s = Student('Ali',450,5)
print(s/1)

#5
class Library:
    def __init__(self,*args):
        self.books=args
    def __len__(self):
        return len(self.books)
lib = Library('Python','Django','SQL')
print(len(lib))

#6
class Temperature:
    def __init__(self,value):
        self.value = value
    def __abs__(self):
        return abs(self.value)
t = Temperature(-25)
print(abs(t))


#8
class Fraction:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Fraction(self.x+other.x,self.y + other.y)
    def __sub__(self, other):
        return Fraction(self.x-other.x,self.y - other.y)
    def __mul__(self, other):
        return Fraction(self.x*other.x,self.y * other.y)
    def __str__(self):
        return f"{self.x,self.y}"
f1 = Fraction(1,2)
f2 = Fraction(1,3)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)


#7
class Cart:
    def __init__(self,items):
        self.items = items
    def __add__(self, other):
        return Cart(self.items+ other.items)
    def __str__(self):
        return f"{self.items}"
c1 = Cart(["olma", "anor"])
c2 = Cart(["banan"])
print(c1 + c2)