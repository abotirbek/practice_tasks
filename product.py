#7
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def sell(self,amount):
        if amount > self.quantity:
            self.quantity = "Sotilmaydi!"
        else:
            self.quantity -= amount

    def update_price(self,new_price):
        if new_price < 0:
            self.price = 'Manfiy!'
        else:
            self.price = new_price

    def get_data(self):
        self.sell(20)
        self.update_price(1300)
        total = self.get_total_price()
        return f"""
{self.name.upper()} narxi: {self.price}, miqdori: {self.quantity}
Jami summa: {total}
"""

product1 = Product('Macbook',1200,100)
print(product1.get_data())