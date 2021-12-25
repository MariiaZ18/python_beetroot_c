# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/ except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    my_list = ['Harry', 'Potter', 'and', 'the', 'Sorcerer\'s', 'Stone']
    print(my_list[6])

def main():
    try:
        oops()
    except IndexError:
        print('List index out of range')


if __name__ == '__main__':
    main()
