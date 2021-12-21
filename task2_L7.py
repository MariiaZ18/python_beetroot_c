# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”


def birthday_greeting():
    your_name = input('Enter your name: ')
    your_age = int(input('Enter your age: '))
    return f'Hello {your_name}, on your next birthday you’ll be {your_age + 1} years'


if __name__ == '__main__':
    print(birthday_greeting())