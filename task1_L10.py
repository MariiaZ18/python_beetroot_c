# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.


def count_unique_words():
    my_input = input('Enter some string: ')
    dict_c = dict()
    words = my_input.split()

    for i in words:
        if i in dict_c:
            dict_c[i] += 1
        else:
            dict_c[i] = 1
    return dict_c


if __name__ == '__main__':
    print(count_unique_words())
