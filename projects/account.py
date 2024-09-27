from decimal import Decimal

class Account:
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        if balance< Decimal(0):
            raise ValueError("balance cannot be less  zero")
        self.balance = balance

    def deposit(self, amount):
        if amount <= self.balance(0.00):
            raise ValueError("amount cannot be less than 0")
        self.balance += amount


a1 = Account("John", Decimal(500))
print(a1.balance)
a1.deposit = 1000
print(a1.balance)


