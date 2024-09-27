from DIARY.Diary import Diary


class DiaryApp:
    name = Diary

    def __init__(self):
        self.diary = Diary

    def show_diary(self):
        print("welcome to the diary app")
        print("What would you like to do?")
        print("1. Create Diary Entry\n2.Unlock\n3.Lock\n4.find Entry\n5.Update entry\n6.Delete Entry\n7.exit")

        choice = int(input("enter your choice: "))

        if choice == 1:
            self.create_entry()
        elif choice == 2:
            self.unlock_entry()
        elif choice == 3:
            self.lock_entry()
        elif choice == 4:
            self.find_entry()
        elif choice == 5:
            self.Update_entry()
        elif choice == 6:
            self.delete_entry()
        elif choice == 7:
            print("Goodbye")
        else:
            print("invalid input")

    def create_entry(self):
        self.diary = Diary(1,"WON")
        title = input("enter title: ")
        body = input("enter body: ")
        self.diary.createEntry(title, body)
        print("ENTRY CREATED")
        print("ENTRY ID IS: ", self.diary.generateId())
        self.show_diary()

    def unlock_entry(self):
        self.diary = Diary("jkjl","kk")
        ID = int(input("enter entry id: "))
        password = input("enter password: ")
        try:
            self.diary.unlockEntry(password)
            print("ENTRY UNLOCKED")
        except Exception as e:
            print(e)
        finally:
            self.show_diary()

    def lock_entry(self):
        self.diary = Diary("VDE", "2222")
        password = input("enter password: ")
        try:
            self.diary.lockEntry(password)
            print("ENTRY IS LOCKED")
        except Exception as e:
            print(e)
        finally:
            self.show_diary()

    def delete_entry(self):
        self.diary = Diary("jf", "3334")
        ID = int(input("enter id: "))
        try:
            self.diary.deleteEntry(ID)
            print("ENTRY IS DELETED")
        except Exception as e:
            print(e)
        finally:
            self.show_diary()

    def Update_entry(self):
        self.diary = Diary("verj", "1111")
        ID = int(input("enter id: "))
        title = input("enter title: ")
        body = input("enter body: ")
        try:
            self.diary.updateEntry(ID, title, body)
            print("ENTRY IS NOW UPDATED")
        except Exception as e:
            print(e)
        finally:
            self.show_diary()

    def find_entry(self):
        self.diary = Diary("DJ", "3344")
        ID = int(input("enter id: "))
        try:
            self.diary.findEntry(ID)
            print("ENTRY IS FOUND")
        except Exception as e:
            print(e)
        finally:
            self.show_diary()


def show_diary():
    init = DiaryApp()
    init.show_diary()


if __name__ == "__main__":
    show_diary()
