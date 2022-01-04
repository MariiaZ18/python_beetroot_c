# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
import random


def common_numbers():
    list_1 = []
    for i in range(0, 10):
        i = random.randint(0, 10)
        list_1.append(i)
    print(f'\nThe first list: {list_1}\n')

    list_2 = []
    for j in range(0, 10):
        j = random.randint(0, 10)
        list_2.append(j)
    print(f'The second list: {list_2}\n')
    result = []
    for h in list_1:
        if h in list_2:
            result.append(h)
        print(f'Exclusive common numbers - {result}')

if __name__ == '__main__':
    common_numbers()
