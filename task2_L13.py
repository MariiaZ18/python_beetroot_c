# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'


class Mathematician:
    def square_nums(self, list_sq: list):
        self.list_sq = list_sq
        list_s = []
        list_s = [i * i for i in list_sq]
        return f'Squares of numbers: {list_s}'

    def remove_positives(self, list_re: list):
        self.list_re = list_re
        list_r = []
        list_r = [i for i in list_re if i < 0]
        return f'Only negative numbers: {list_r}'

    def filter_leaps(self, list_le):
        self.list_le = list_le
        list_l = []
        list_l = [i for i in list_le if i % 4 == 0]
        return f'Leap years: {list_l}'


m = Mathematician()
a = [7, 11, 5, 4]
b = [26, -11, -8, 13, -90]
c = [2001, 1884, 1995, 2003, 2020]
print(a, m.square_nums([7, 11, 5, 4]))
print(b, m.remove_positives([26, -11, -8, 13, -90]))
print(c, m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
