# School
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.
class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_name_for_email(self):
        f_n = f'{self.first_name}{self.last_name}'
        return f_n.lower()

    def make_email(self):
        return f'{self.full_name_for_email()}' + '@gmail.com'


class Student(Person):
    def __init__(self, first_name, last_name, age, year_of_study: int, st_prog: str, type_st: str, university: str,
                 tel_num: int):
        super().__init__(first_name, last_name, age)
        self.year_of_study = year_of_study
        self.st_prog = st_prog
        self.type_st = type_st
        self.university = university
        self.tel_num = tel_num

    def get_info(self):
        return f'\n{self.full_name()}  {self.age} y o.\nStudies at {self.university}.\nType of study: {self.type_st}.\nStudy programme: {self.st_prog}.\nTelephone number: {self.tel_num}\nEmail: {self.make_email()}'


class Teacher(Person):
    def __init__(self, first_name, last_name, age, teaches: str, tel_num: int):
        super().__init__(first_name, last_name, age)
        self.teaches = teaches
        self.tel_num = tel_num

    def get_info(self):
        return f'{self.full_name()} {self.age} y.o.\nTeaches: {self.teaches}\nTelephone number: {self.tel_num}\nEmail: {self.make_email()}'


person1 = Student('Mariia', 'Zeikan', 19, 2, 'Computer Science', 'Bachelor', 'Techical University of Ostrava',
                  778569007)
print(person1.get_info())
print()
person2 = Teacher('Yulia', 'Kormosh', 35, 'Logic', 773985004)
print(person2.get_info())
