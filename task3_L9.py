# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

def are_dev():
    list0 = []
    for j in range(101):
        list0.append(j)
    print(list0, end='\n\n')

    list = []
    for i in range(101):
        if i % 7 == 0 and i % 5 != 0:
            list.append(i)

    print(list, end='\n\n')


if __name__ == '__main__':
    are_dev()
