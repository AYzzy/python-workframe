import unittest

from projects.BankApp import account, bank
# from projects.BankApp import bank
from projects.BankApp.bank import Bank
from projects.BankApp.account import Account

# def function_for_invalid_pin():
#     raise ValueError("The amount cannot be less than Balance")


class TestBankApp(unittest.TestCase):

    # def __init__(self, methodName: str = "runTest"):
    #     super().__init__(methodName)
    #     self.Account = None

    def setUp(self):
        self.bank = Bank("UBA", pin="2233")

    def test_to_register_account(self):
        self.bank.register_new_account("AYO", "Mide", "1234")
        self.assertEqual(1, self.bank.get_Account())

    def test_to_deposit_to_account(self):
        self.bank.registered_user(1, "ayo", "mide")
        self.bank.deposit(1, 2000)
        self.assertEqual(2000, self.bank.get_Balance())

    def test_to_register_more_than_one_account(self):
        self.bank.register_new_account("ayo", "mide", "2233")
        self.bank.register_new_account("mesh", "    Yaro", "6655")
        self.bank.register_new_account("fitz", "Gerad", "8899")
        self.assertEqual(3, self.bank.get_Account())

    def test_to_withdraw_from_account(self):
        self.bank.registered_user(1, "mesh","Yaro")
        self.bank.deposit(1, 6000)
        self.bank.withdraw(3000, "2233", 1)
        self.assertEqual(3000, self.bank.get_Balance())

    def test_to_withdraw_with_above_balance(self):
        self.bank.register_new_account("AYO", "Mide", "1234")
        self.bank.deposit(1, 7000)
        self.assertRaises(ValueError, lambda: Bank.withdraw())

