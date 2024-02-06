class Person:
    def __init__(self, name):
        self.name = name
    def SayMyName(self):
        print("моє імя" + self.name)
    def ChangeName(self, name):
        self.name = name
        print("Моє нове ім'я: " + name)