from DIARY.Entry import Entry


class Diary:

    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password
        self.Unlocked = True
        self.entries = []
        self.counter = 0

    def generateId(self):
        self.counter = self.counter + 1
        return self.counter

    def createEntry(self, title, body):
        ID = self.generateId()
        entry = Entry(ID, title, body)
        self.entries.append(entry)
        return entry

    def getEntriesSize(self):
        return len(self.entries)

    def deleteEntry(self,ID):
        for entry in self.entries:
            if entry.ID == ID:
                self.entries.remove(entry)
            if entry.ID < ID:
                raise ValueError("Entry does not exist")
            if entry.ID > ID:
                raise ValueError("Entry does not exist")

    def findEntry(self,ID):
        for entry in self.entries:
            if entry.ID == ID:
                return entry

    def updateEntry(self, ID, title, body):
        for entry in self.entries:
            if entry.id == ID and entry.title == title and entry.body == body:
                return entry

    def unlockEntry(self, password):
        if self.Password != password:
            raise ValueError("wrong password")
        return self.Password

    def lockEntry(self, password):
        return self.Password == password
