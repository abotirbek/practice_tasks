#4
class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def apply_discount(self,percent):
        if not 0<percent<=50:
            print("Chegirma qo'llanilmadi")
        else:
            self.price = self.price *(100-percent)//100

    def get_info(self):
        self.apply_discount(51)
        return f"""
Brand: {self.brand.upper()}
Model: {self.model.capitalize()}
Narx: ${self.price}
"""

phone1 = Phone("Apple",'iPhone 17',1200)
print(phone1.get_info())
