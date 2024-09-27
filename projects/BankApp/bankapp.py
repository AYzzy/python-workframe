from projects.BankApp.bank import Bank


class BankApp:
    def __init__(self):
        self.balance = 0
        self.bank = Bank("Yzzy ", "6777")

    def display(self):
        print("Welcome to the BankApp")
        print("What would you like to do?")
        print("1. Create a bank account")
        print("2. Deposit money to your account")
        print("3. Withdraw money from your account")
        print("4. Transfer money from your account")
        print("5. CheckBalance")
        print("6. Delete your account")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.registered_user()
        elif choice == 2:
            self.deposit()
        elif choice == 3:
            self.withdraw()
        elif choice == 4:
            self.Transfer()
        elif choice == 5:
            self.Check_Balance()
        elif choice == 6:
            self.Delete_Account()
        elif choice == 7:
            self.End_Program()
        else:
            print("Invalid selection input")

    def registered_user(self):
        first_Name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        pin_number = input("Enter your new pin number: ")
        account = self.bank.register_new_account(first_Name, last_name, pin_number)
        print("Account Created")
        print("Your account number is ", account.get_number())
        self.display()

    def deposit(self):
        account_number = int(input("Enter your existing account number: "))
        amount_to_deposit = int(input("Enter amount to deposit: "))
        try:
            self.bank.deposit(int(account_number), int(amount_to_deposit))
            print("YOU HAVE SUCCESSFULLY DEPOSITED")
        except Exception as e:
            print(e)
        finally:
            self.display()

    def withdraw(self):
        account_number = int(input("Enter your existing account number: "))
        amount_to_withdraw = int(input("Enter amount to withdraw:"))
        pin = input("Enter your pin: ")
        try:
            self.bank.withdraw(int(amount_to_withdraw), str(pin), int(account_number))
            print("YOU HAVE SUCCESSFULLY WITHDRAWN")
        except Exception as e:
            print(e)
        finally:
            self.display()

    def Transfer(self):
        amount = int(input("Enter your existing account number: "))
        sender_acc = int(input("Enter amount to withdraw:"))
        receiver_acc = input("Enter receiver account number: ")
        pin_number = input("Enter your pin number: ")
        try:
            self.bank.transfer(int(amount), int(sender_acc), int(receiver_acc), pin_number)
            print("YOU HAVE SUCCESSFULLY TRANSFERRED TO THE OTHER ACCOUNT")
        except Exception as e:
            print(e)
        finally:
            self.display()

    def Check_Balance(self):
        account_number = int(input("Enter your existing account number: "))
        pin_number = input("Enter your existing pin number:")
        try:
            self.bank.check_balance(int(account_number), str(pin_number))
            print("YOUR BALANCE IS", self.balance)
        except Exception as e:
            print(e)
        finally:
            self.display()

    def Delete_Account(self):
        account_number = int(input("Enter your existing account number:"))
        pin_number = input("Enter your existing pin number:")
        try:
            self.bank.deleteAccount(int(account_number), pin_number)
            print("YOU HAVE SUCCESSFULLY DELETED THIS ACCOUNT")
        except Exception as e:
            print(e)
        finally:
            self.display()

    @staticmethod
    def End_Program():
        print("Exiting Program")


def display():
    bank = BankApp()
    bank.display()


if __name__ == "__main__":
    display()
