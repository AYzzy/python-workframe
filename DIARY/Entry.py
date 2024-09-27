import datetime


class Entry:
    def __init__(self, id, title, Body):
        self.title = title
        self.Body = Body
        self.id = id
        self.dateCreated = datetime

    def getID(self):
        return self.id

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.Body

    def getDateCreated(self):
        return self.dateCreated
