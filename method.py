class Phone:
    def __init__(self,title,price):
        self.title=title
        self.price=price

    def get_info(self):
        return f"{self.title} narxi ${self.price}"

obj=Phone('iPhone',500)
obj2=Phone('Nokia',200)
obj3=Phone('Redmi',100)
obj4=Phone('iPhone',1000)

class Market:
    def __init__(self,title):
        self.title=title
        self.phones=[]

    def add_phone(self,*args):
        for x in args:
            if isinstance(x, Phone):
                self.phones.append(x)
            else:
                print('Bizni aldama')

    def get_phones(self):
        for o in self.phones:
            print(o.get_info())


    def find_expensive(self):
        prices = []
        for x in self.phones:
            prices.append(x.price)
        min_price=min(prices)
        for x in self.phones:
            if x.price==min_price:
                print(x.get_info())
        #nested
        min_p=min([x.price for x in self.phones])
        data=[x.get_info() for x in self.phones if x.price == min_p]
        print(data[0])

    def get_all_info(self):
        length = len(self.phones)
        total = sum([x.price for x in self.phones])
        maximum = max([x.price for x in self.phones])
        data1 = [x.get_info() for x in self.phones if x.price == maximum]
        minimum = min([x.price for x in self.phones])
        data2 = [x.get_info() for x in self.phones if x.price == minimum]
        return f"""
Jami mahsulot soni: {length} dona
Jami summa: ${total}
Eng qimmati: {data1[0]}
Eng arzoni: {data2[0]}
"""

dokon = Market("Malika A1")
dokon.add_phone(obj,obj2,obj3,obj4)
# print(dokon.get_phones())
print(dokon.get_all_info())