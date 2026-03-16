#1
class SmartCounter:
    def __init__(self,number):
        self.num = number
        self.count = 0
        self.total_objects()
    # @classmethod
    def total_objects(self):
        self.count += 1
        return self.count
    @staticmethod
    def is_positive(new):
        if new < 0:
            return f"{new} is Negative"
        elif new > 0:
            return f"{new} is Positive"
        else:
            return f"{new} is Zero"
    def __str__(self):
        return f"{self.count} - object is {self.num}"
    def __repr__(self):
        return f"{self.count}-obj: {self.num}"
c1 = SmartCounter(10)
c2 = SmartCounter(-5)
print(c1.is_positive(10))
print(c1)
print(repr(c1))
print(c1.total_objects())
print(c2.is_positive(-5))
print(c2)
print(repr(c2))
print(c2.total_objects())

#2
class Money:
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency
    def __add__(self,other):
        return self.amount + other.amount
    def __sub__(self,other):
        return self.amount - other.amount
    def __mul__(self,other):
        return self.amount * other
    def __eq__(self,other):
        return self.amount == other
m1 = Money(100, "USD")
m2 = Money(50, "USD")

print(m1 + m2)
print(m1 - m2)
print(m1 * 3)
print(m1 == Money(100, "USD"))

#3
class UserProfile:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def __getattr__(self, item):
        return f"Bunday atribut yo'q"
    def __setattr__(self, key, value):
        if key == 'password':
            value = "Taqiqlangan"
            return super().__setattr__(key, value)
        else:
            return super().__setattr__(key,value)
u = UserProfile("Ali", "ali@gmail.com")
u.password = "12345"

print(u.name)
print(u.age)
print(u.password)




#4
class CustomList:
    def __init__(self,items):
        self.items = items
    def __getitem__(self,index):
        if index < len(self.items):
            return self.items[index]
        else:
            return f"{index} is not avilable"
    def __setitem__(self,index,value):
        self.items[index]=value
    def __len__(self):
        return len(self.items)
cl = CustomList([10, 20, 30])

print(cl[1])
cl[1] = 99
print(cl[1])
print(len(cl))
print(cl[10])

#5
class InventoryItem:
    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __add__(self, other):
        if other is int:
            return self.quantity + other
    def __getattr__(self, item):
        return f"{item} is not available"
    def __getitem__(self, item):
        return self.


i1 = InventoryItem("Laptop", 1000, 5)
i2 = InventoryItem("Laptop", 1000, 3)
print(type(i1))
print(i1 + i2)
print(i1["price"])
i1["quantity"] = 10