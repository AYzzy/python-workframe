
class BankApp:
    def __init__(self):
        self.bank_App = BankApp()


    def main(self):
        print("Welcome to the Bank")
        print("What would you like to do?")
        print("1. Create a bank account")
        print("2. Deposit money to your account")
        print("3. Withdraw money from your account")
        print("4. Transfer money from your account")
        print("5. CheckBalance")
        print("6. Delete your account")
        print("7. Exit")

    def display_bank(self):
        while True:
            self.display_bank()
            choice = input("Enter your choice: ")
            if choice == 1:
                first_Name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                account_number = input("Enter your account number: ")
                pin_number = input("Enter your new pin number: ")
                self.bank_App.add_account(first_Name,last_name,pin_number)
                print("Account Created")
                print("-"*30)

            elif choice == 2:
                account_number = int(input("Enter your existing account number: "))
                amount_to_deposit = int(input("Enter amount to deposit: "))
                self.bank_App.deposit(account_number,amount_to_deposit)
                print("YOU HAVE SUCCESSFULLY DEPOSITED")


            elif choice == 3:
                account_number = int(input("Enter your existing account number: "))
                amount_to_withdraw = int(input("Enter amount to withdraw:"))
                pin_number = input("Enter your pin: ")
                self.bank_App.withdraw(account_number,amount_to_withdraw)
                print("YOU HAVE SUCCESSFULLY WITHDRAWN")

            elif choice == 4:
                account_number = int(input("Enter your existing account number: "))
                amount_to_withdraw = int(input("Enter amount to withdraw:"))
                pin_number = input("Enter your pin: ")
                amount_to_deposit = int(input("Enter amount to other account number: "))
                self.bank_App.transfer(account_number,amount_to_withdraw,pin_number,amount_to_deposit)
                print("YOU HAVE SUCCESSFULLY TRANSFERRED TO THE OTHER ACCOUNT")

            elif choice == 5:
                account_number = int(input("Enter your existing account number: "))
                pin_number = input("Enter your existing pin number:")
                self.bank_App.balance(account_number,pin_number)
                print("YOUR BALANCE IS",self.balance)

            elif choice == 6:
                account_number = int(input("Enter your existing account number:"))
                pin_number = input("Enter your existing pin number:")
                self.bank_App.deletedAccount(account_number,pin_number)
                print("YOU HAVE SUCCESSFULLY DELETED THIS ACCOUNT")

            elif choice == 7:
                print("Exiting Program")
                break
            else:
                print("Invalid selection input")

    def add_account(self, first_Name, last_name, pin_number):
        pass


