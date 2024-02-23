from decimal import Decimal
class Account2:

    # the self is the argument to the class
    def __init__(self, name, balance: Decimal):
        self.name = name
        self.balance = balance
    # the @property can be used to decorate another method in the class
    @property
    def balance(self):
        return self._balance

    # 
    @balance.setter
    def balance(self, balance):
        if balance < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self._balance = balance

    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}"

a1 = Account2('Dayo', Decimal(100))

print(a1)
