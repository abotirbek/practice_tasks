#1
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


class Car(Vehicle):
    def __init__(self, name, speed):
        Vehicle.__init__(self, name, speed)

    def honk(self):
        return "Bip-bip"


class Bicycle(Vehicle):
    def __init__(self, name, speed):
        Vehicle.__init__(self, name, speed)

    def pedal(self, times):
        return f"The bicycle has been pedalled {times} times"


class Truck(Vehicle):
    def __init__(self, name, speed):
        Vehicle.__init__(self, name, speed)

    def load_cargo(self):
        return "Cargo is being loaded ...\nIt has been loaded"

car = Car('Mc Queen', 80)
truck = Truck('Brave', 40)
bike = Bicycle('Speedy', 15)
print(car.honk())
print(truck.load_cargo())
print(bike.pedal(20))

#2
class Animal:
    def make_sound(self):
        return "The animal makes a sound"

class Lion(Animal):
    def roar(self):
        return "The lion roars"
    def make_sound(self):
        return self.roar()

class Eagle(Animal):
    def screech(self):
        return "The eagle screeches"
    def make_sound(self):
        return self.screech()

class Shark(Animal):
    def splash(self):
        return "The shark splashes"
    def make_sound(self):
        return self.splash()

lion = Lion()
eagle = Eagle()
shark = Shark()
print(lion.make_sound())
print(eagle.make_sound())
print(shark.make_sound())

#3
class Employee:
    def __init__(self, monthly_salary):
        self.month = monthly_salary
        self.hour = hourly_rate
        self.day = daily_rate
        self.week = weekly_rate
    def get_salary(self):
        return f"Monthly salary: {monthly_salary}"

class Manager(Employee):
    def __init__(self, weekly_rate, weeks_worked):
        Employee.__init__(self, monthly_salary)
        self.week = weekly_rate
        self.amount = weeks_worked
    def get_salary(self):
        return f"Weekly salary: {self.week * self.amount}"

class Developer(Employee):
    def __init__(self, daily_rate, days_worked):
        Employee.__init__(self, monthly_salary)
        self.day = daily_rate
        self.amount = days_worked

    def get_salary(self):
        return f"Daily salary: {self.day * self.amount}"

class Designer(Employee):
    def __init__(self, hourly_rate, hours_worked):
        Employee.__init__(self, monthly_salary)
        self.hour = hourly_rate
        self.amount = hours_worked

    def get_salary(self):
        return f"Hourly salary: {self.hour * self.amount}"

#4
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, name, price):
        Product.__init__(self, name, price)
    def apply_discount(self):
        return f"Discounted price for {self.name}: ${self.price * 0.9}"

class Clothing(Product):
    def __init__(self, name, price):
        Product.__init__(self, name, price)
    def get_prize(self):
        if self.price > 100:
            return f"You get an extra T-shirt"
        else:
            return f"You get extra 5 pairs of socks"

class Food(Product):
    def __init__(self, name, price, active_days):
        Product.__init__(self, name, price)
        self.active_days = active_days
    def check_expiry(self):
        return f"Validity period: {self.active_days} days"

#5
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        BankAccount.__init__(self, balance)
    def withdraw(self, amount):
        self.balance -= amount
        return f"Taken: ${amount},\nRemaining: ${self.balance}"

class CheckingAccount(BankAccount):
    def __init__(self, balance):
        BankAccount.__init__(self, balance)
    def withdraw(self):
        return f"You have ${self.balance} in your bank account"