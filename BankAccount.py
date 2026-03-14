#3
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount <=0:
            return "Faqat musbat!"
        else:
            return amount

    def withdraw(self,amount):
        if amount > self.balance:
            return "Balansdan ko'p yechib bo'lmaydi"
        else:
            return 'Bajarildi!'


    def get_balance(self):
        return f"{self.owner.capitalize()} balans: ${self.balance}"

owner1 = BankAccount('ali',100)
print(owner1.get_balance())
print(owner1.deposit(-1))
print(owner1.withdraw(120))