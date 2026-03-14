#2
class Book:
    def __init__(self,author,title,price):
        self.author = author
        self.title=title
        self.price=price

    def get_info(self):
        if self.price < 0:
            self.price = "Manfiy xato"
        else:
            self.price = f"${self.price}"
        return f"""
{self.author}ning \"{self.title}\" kitobi {self.price}
"""
    def new_price(self,x):
        if x <= 0:
            return "Manfiy xato"
        elif x == 2*self.price:
            return "2 marta qimmat!"
        else:
            self.price = x
            return self.price


book1 = Book('Robert','Rich dad, Poor dad',120)
print(book1.new_price(240))
print(book1.get_info())