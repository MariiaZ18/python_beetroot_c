# School
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.

class People:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

        # For call to str(). Prints readable form

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    def make_email(self):
        maked_email = f'{self.full_name_for_em()}' + '@gmail.com'
        print('Email: ')
        return maked_email.lower()

    def full_name_for_em(self):
        full_name_for_e = f'{self.first_name}{self.last_name}'
        return full_name_for_e


class Student(People):

    def __init__(self, first_name: str, last_name: str, age: int, year_of_studies: int, specialty: str):
        super().__init__(first_name, last_name, age)
        self.year_of_studies = year_of_studies
        self.specialty = specialty

    def student_info(self):
        info = f'\n{self.full_name()} {self.age}, years old.\nStudies at the university VSB-TUO.\nStudy programme: {self.specialty}'
        return info


class Teacher(People):
    def __init__(self, first_name: str, last_name: str, age: int, teaches: str):
        super().__init__(first_name, last_name, age)
        self.teaches = teaches

    def return_info(self):
        return f'{self.full_name()}.\nTeaches: {self.teaches}'


kaja = Student('Karolína', 'Skokanová', 20, 1, 'Computer Science')
print(kaja.student_info())
print(kaja.make_email().__repr__())
print()
test = Teacher('Lesia', 'Zeikan', 54, 'Logic for informatics')
print(test.return_info())
print(test.make_email())
