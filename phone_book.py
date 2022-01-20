"""
Extend Phonebook application
Functionality of Phonebook application:
Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
The first argument to the application should be the name of the phonebook. Application should load JSON data,
if it is present in the folder with application, else raise an error. After the user exits, all data should be saved to loaded JSON.
"""
import json
import pathlib


class Phone_Book:

    def __init__(self, name, surname, tel, city, state):
        self.name = name
        self.surname = surname
        self.tel = tel
        self.city = city
        self.state = state

    def full_name(self):
        print(f'{self.name} {self.surname}')

    def full_info(self):
        full_info_person = f'{self.full_name()} {self.tel} {self.city} {self.state}'
        return full_info_person


Mariia = Phone_Book('Mariia', 'Zeikan', 773937004, 'Ostrava', 'CZ')
Petro = Phone_Book('Petro', 'Zeikan', 778532457, 'Ostrava', 'CZ')
Yulia = Phone_Book('Yulia', 'Kormosh', 772598456, 'Praha', 'CZ')
Volodymyr = Phone_Book('Volodymyr', 'Gorzov', 97251478, 'Lviv', 'UA')
str_1 = json.dumps(Mariia.__dict__)
str_2 = json.dumps(Petro.__dict__)
str_3 = json.dumps(Yulia.__dict__)
str_4 = json.dumps(Volodymyr.__dict__)
pole = [str_1, str_2, str_3, str_4]

with open('data.json', 'w') as data_from_file:
    for line in pole:
        data_from_file.write(line)
        data_from_file.write('\n')
    data_from_file.close()


def show_menu():
    print("""
        1: Search by first name
        2: Search by last name
        3: Search by full name
        4: Search by telephone number
        5: Search by city or state
        6: Delete a record for a given telephone number
        7: Update a record for a given telephone number  
        8: Quit""")


def alg_fun():
    while True:
        path_to_this_file = pathlib.Path(__file__)
        path_to_parent = path_to_this_file.parent
        path_to_another_file = path_to_parent.joinpath('data.json')
        data_from_file = path_to_another_file.read_text()
        selection = input('Please make your selection from the options above: ')
        if selection == '1':
            a = str(input('Enter a name: '))
            if a in data_from_file:
                find(a)
            else:
                print('A person with this name was not found')
        if selection == '2':
            a = str(input('Enter a surname: '))
            if a in data_from_file:
                find(a)
            else:
                print('A person with this surname was not found')
        if selection == '3':
            a = str(input('Enter a full name of person: '))
            if a in data_from_file:
                find(a)
            else:
                print('A person not found: ')
        if selection == '4':
            a = (input('Enter a telephone number: '))
            if a in data_from_file:
                find(a)
            else:
                print('A person not found: ')
        if selection == '5':
            a = str(input('Enter a city or state: '))
            if a in data_from_file:
                find(a)
            else:
                print('A person not found: ')
        if selection == '6':
            a = str(input('Enter a telephone number: '))
            if a in data_from_file:
                with open('data.json', 'w+') as data_from_file:
                    read_line = data_from_file.readline()
                    if a in read_line:
                        read_line.replace('"[', '[').replace(']"', ']')
                    data_from_file.close()
        if selection == '8':
            print('\n' + 'Goodbye, see you soon')
            break


def find(a):
    my_list = []
    with open('data.json', 'rt') as file:
        data_from_file = file.readlines()
    for line in data_from_file:
        if a in line:
            my_list.append(line)
    print(my_list)


if __name__ == '__main__':
    show_menu()
    alg_fun()
