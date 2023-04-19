
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Au Au Au!"

class Cat(Animal):
    def make_sound(self):
        return "Miau!"

animals = [Dog("Tigor", "preto"), Dog("LILIca", "preta"), Dog("Belinha", "Branca"), Cat("Teo", "cinza"), Cat("Astolfo", "Marrom Claro")]

for animal in animals:
    print(animal.name +' '+ animal.color + ": " + animal.make_sound())