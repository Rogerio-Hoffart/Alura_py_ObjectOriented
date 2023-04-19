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


animals = [Dog("Tigor", "preto"), Dog("LILIca", "preta"), Dog("Belinha", "Branca"), Cat("Teo", "cinza"),
           Cat("Astolfo", "Marrom Claro")]

for animal in animals:
    print(animal.name + ' ' + animal.color + ": " + animal.make_sound())


class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2


class Triangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height) / 2


shapes = [Rectangle("blue", 5, 10), Circle("red", 7), Triangle("yelow", 5, 10)]

for shape in shapes:
    print(shape.color + " " + str(shape.area()))
