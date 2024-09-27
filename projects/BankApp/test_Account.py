import unittest

from projects.BankApp.account import Account
from projects.BankApp.exception import InvalidAmountError


class TestAccount(unittest.TestCase):

    def test_account_as_zero_balance(self):
        account = Account("John", "2233", 334455)
        self.assertEqual(0, account.balance)

    def test_to_deposit_in_account(self):
        account = Account("John", "2233", 334455)
        account.deposit(5000)
        self.assertEqual(5000, account.balance)

    def test_to_deposit_twice_in_account(self):
        account = Account("John", "2233", 334455)
        account.deposit(5000)
        account.deposit(4000)
        self.assertEqual(9000, account.balance)

    def test_to_deposit_a_negative_amount_in_account(self):
        account = Account("John", "2233", 334455)
        self.assertRaises(ValueError, lambda: account.deposit(-5000))
        self.assertEqual(0, account.balance)

    def test_to_withdraw_in_account(self):
        account = Account("John", "2233", 334455)
        account.deposit(6000)
        account.withdraw(3000, "2233", 334455)
        self.assertEqual(3000, account.balance)

    def test_withdraw_in_account_twice(self):
        account = Account("John", "2233", 334455)
        account.deposit(7000)
        account.withdraw(2000, "2233", 334455)
        account.withdraw(3000, "2233", 334455)
        self.assertEqual(2000, account.balance)

    def test_withdraw_amount_twice_one_correct_and_one_wrong_pin(self):
        account = Account("John", "2233", 334455)
        account.deposit(7000)
        account.withdraw(2000, "2233", 334455)
        self.assertEqual(5000, account.balance)
        self.assertRaises(ValueError, lambda: account.withdraw(3000, "2234", 334455))

    def test_withdraw_amount_above_balance(self):
        account = Account("John", "2233", 334455)
        account.deposit(3000)
        self.assertEqual(3000, account.balance)
        self.assertRaises(ValueError, lambda: account.withdraw(4000, "2233", 334455))

    def test_to_check_balance(self):
        account = Account("John", "2233", 334455)
        account.deposit(8000)
        account.deposit(6000)
        account.check_balance("2233", 334455)
        self.assertEqual(14000, account.balance)

    def test_check_balance_with_wrong_pin(self):
        account = Account("John", "2233", 334455)
        account.deposit(6000),
        self.assertRaises(ValueError, lambda: account.check_balance("223", 334455))
