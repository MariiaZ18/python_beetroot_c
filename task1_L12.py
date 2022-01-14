# Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing, for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age_1(self):
        return f'Age - {self.age}'

    @property
    def talk(self):
        return f'Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old'


def main():
    yuliia = Person(first_name='Yuliia', last_name='Kormosh', age=18)
    print('\n')
    print(yuliia.talk)


if __name__ == '__main__':
    main()
