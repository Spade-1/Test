# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("Move")
#     def draw(self):
#         print("Draw")

# point = Point(10, 20)
# print(point.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi I'm {self.name}")

# john = Person("John Smith")
# john.talk()

# bob = Person("Bob Smith")
# bob.talk()

class Mammal:
    def walk(self):
        print("Walk")
class Dog(Mammal):
    def bark(self):
        print("Woof Woof")
class Cat(Mammal):
    def meow(self):
        print("Meow Meow")

dog = Dog()
dog.walk()
dog.bark()
cat = Cat()
cat.meow()

    