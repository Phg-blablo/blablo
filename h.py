class Person:
    def print(self):
        print("Name:", self.name)
        print("Age:", self.age)
    def __init__(self, n, a):
        self.name = n
        self.age = a
macron = Person("Emmanuel Macron",45)
macron.print()