class Human:
    number_of_eye = 2

    def __init__(self, height: float, gender: str, name: str):
        self.height = height
        self.gender = gender
        self.name = name

    def sleep(self):
        print(f"{self.name} Sleeping.....")

    def eat(self):
        print("Eating....")

    def __str__(self):
        return f"{self.name} is {self.gender}"


h1 = Human(50, "male", 'bolaji')
h2 = Human(33, "female", 'hannah')
h3 = Human(50, "male", 'tolu')

print(h3.number_of_eye)
print(h1.number_of_eye)
print(h2.number_of_eye)


name = 'dayo'
print(type(name))
print(h1.sleep())
print(h2.sleep())


print(h1)
print(h2)