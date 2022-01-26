# Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.

class Animal:

    def __init__(self, name: str):
        self.name = name

    def talk(self):
        print('Talk')


class Dog(Animal):
    atr = 'dog'

    def __init__(self, name):
        Animal.__init__(self, name)

    def talk(self):
        print('Woof Woof ')

    def print_name(self):
        print(f"Hello, my name is {self.name}")


class Cat(Animal):
    atr = 'cat'

    def __init__(self, name):
        Animal.__init__(self, name)

    def print_name(self):
        print(f"Hello, my name is {self.name}")

    def talk(self):
        print('Meow')


c = Cat('Roze')
d = Dog('Simon')
l = [c, d]
for i in l:
    i.print_name()
    print('I am a' + ' ' + i.atr)
    i.talk()
