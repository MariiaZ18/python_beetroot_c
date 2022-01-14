# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j) where ''i goes from 1 to 10 and 'j' is corresponding to 'i' squared.

def main():
    my_list = [(i, i ** 2) for i in range(10)]

    return my_list

if __name__ == '__main__':
    print(main())