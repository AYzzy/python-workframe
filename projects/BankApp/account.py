
class Account:

    def __init__(self, name, pin, number):
        """

        :rtype: object
        """
        self.name = name
        self.pin = pin
        self.number = number
        self.balance = 0

    def get_number(self):
        return self.number

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount
        return self.balance

    def withdraw(self, amount, pin, number):
        if self.balance > amount < 0:
            raise ValueError("invalid amount to withdraw or Insufficient fund")
        if not self.pin == pin:
            raise ValueError("incorrect pin")
        if not self.number == number:
            raise ValueError("incorrect number")
        self.balance = self.balance - amount

    def check_balance(self, pin, number):
        if not self.number == number:
            raise ValueError(" invalid account number")
        if self.pin != pin:
            raise ValueError("incorrect pin")
        return self.balance


# def deposit(amount):
#     if amount < 0:
#         raise ValueError("Sorry you can't deposit negative amount")

