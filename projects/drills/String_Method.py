class StringMethod:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        return self.string.upper()

    def __str__(self):
        return f'{self.string.upper()}'


