class Phonebook:
    def __init__(self):
        self.phone_book = Phonebook()

    def menu(self):
        print("1. Add contact")
        print("2. Get number")
        print("3. Delete contact")
        print("4. Exit")


    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter contact name: ")
                number = input("Enter contact number: ")
                self.phone_book.add_contact (name, number)
                print("Contact added successfully.")
            elif choice == "2":
                name = input("Enter contact name: ")
                number = self.phone_book.get_number(name)
                if number:
                    print(f"The number for {name} is: {number}")
                else:
                    print(f"No number found for {name}.")
            elif choice == "3":
                name = input("Enter contact name: ")
                self.phone_book.delete_contact(name)
                print("Contact deleted successfully.")
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")






