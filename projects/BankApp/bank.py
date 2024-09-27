from projects import account
from projects.BankApp.account import Account


class Bank:

    def __init__(self, name, pin):
        self.pin = pin
        self.name = name
        self.account = []
        self.counter =1
        self.balance = 0

    def register_new_account(self, first_name: str, last_name: str, pin: str):
        account_number = self.generate_number()
        new_account = Account(first_name + " " + last_name, pin, account_number)
        self.account.append(new_account)
        return new_account

    def generate_number(self):
        self.counter += 1
        return self.counter

    def get_Account(self):
        return len(self.account)

    def registered_user(self, account_number, first_name, last_name):
        for Account in self.account:
            if Account == account_number:
                return Account

    def deposit(self, account_number: int, amount: int):
        account = self.find_account(account_number)
        self.balance += amount
        if amount > self.balance:
            raise ValueError("Amount cannot be less than Balance")
        elif account not in self.account:
            raise ValueError("NO ACCOUNT FOUND")
        return self.balance

    def get_Balance(self):
        return self.balance

    def check_balance(self, pin: str, account_number: int):
        account=self.find_account(account_number)
        account.check_balance(pin, account_number)

    def withdraw(self, amount: int, pin: str, account_number: int):
        account = self.find_account(account_number)
        account.withdraw(amount, pin, account_number)

    def find_account(self, account):
        for acc_number in self.account:
            if acc_number == acc_number:
                return acc_number

    def deleteAccount(self, account_number: int, pin_number: str):
        for account in self.account:
            if account == account_number:
                if self.pin == pin_number:
                    account.remove(account_number)
                else:
                    raise ValueError("incorrect pin")

    def transfer(self, amount: int, sender_acc: int, receiver_acc: int, pin_number: str):
        sender_acc = self.find_account(sender_acc)
        receiver_acc = self.find_account(receiver_acc)
        sender_acc.withdraw(amount, pin_number)
        receiver_acc.deposit(amount)


