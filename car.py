#5
class Car:
    def __init__(self,brand,year,color):
        self.brand = brand
        self.year = year
        self.color = color

    def update_year(self,new_year):
        if new_year < self.year:
            print("Xato!")
        else:
            self.year = new_year

    def get_info(self):
        self.update_year(2020)
        if self.year == 2023:
            self.year = "Noma'lum yil"
        elif self.year < 2000:
            return "2000dan kichik mumkin emas"
        return f"""
{self.year}da ishlab chiqarilgan {self.color.lower()} rangli {self.brand}
"""
car1 = Car('Chevrolet',2021,'white')
print(car1.get_info())
