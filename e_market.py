class Product:
    def __init__(self,price):
        self.__price = price

    @classmethod
    def set_discount(cls,percent):
        result = cls.__price * (1-percent/100)
        return result

    @staticmethod
    def calculate_tax(amount):
        amount *= 0.95
        return amount

    def get_price(self):
        return f"Hozirgi narx: {self.__price}"
p1 = Product(1000)
Product.set_discount(10)  # 10% chegirma
print(p1.get_price())  # 900
print(Product.calculate_tax(900))