class Gm:
    SHIORI = 'olg\'aaaaa'
    REGION = 'Andijon'
    COUNT = 0

    def __init__(self,brand,model,engine,price):
        self.brend = brand
        self.model = model
        self.mator = engine
        self.narx = price
        Gm.COUNT += 1

    def warn(self):
        if Gm.COUNT == 5:
            print("Obyektlar soni 5tadan oshib ketdi")

    def raise_price(self,x):
        if x < 0 or x <= self.narx:
            print("Arzonroq bo'lishi mumkin emas")
        else:
            self.narx=x

    def add_thousand(self):
        self.narx += 1000

    def get_data(self):
        return f"""
Model: {self.model.title()}
Brend: {self.brend.upper()}
Motor: *{self.mator}*
Narx: ${self.narx}
"""

obj1 = Gm('General Motors','Onix Turbo', '1.5 atmosferniy', 16000)
obj2 = Gm('General Motors','Onix Turbo', '1.5 atmosferniy', 16000)
obj3 = Gm('General Motors','Onix Turbo', '1.5 atmosferniy', 16000)
obj4 = Gm('General Motors','Onix Turbo', '1.5 atmosferniy', 16000)
obj5 = Gm('General Motors','Onix Turbo', '1.5 atmosferniy', 16000)
obj6 = Gm('General Motors','Onix Turbo', '1.5 atmosferniy', 16000)

obj1.raise_price(14000)
# obj2 = Gm('General Motors', 'Damas','1.4',8000)
print(obj1.get_data())
print(obj2.get_data())
print(obj3.get_data())
print(obj4.get_data())
print(obj5.get_data())
print(obj6.get_data())






# print(obj.narx)
# print(obj.model)
# obj3 = Gm()
# obj.title = 'onix'
# obj2.title = 'nexia'
# obj3.title = 'onix'
# print(obj.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)