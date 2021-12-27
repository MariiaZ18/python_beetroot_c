# The greatest number
# # Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
import random


def greatest_number():
    my_list = []
    for i in range(0, 10):
        i = random.randint(1, 2555)
        my_list.append(i)
    print(my_list)
    max_of_my_list = max(my_list)
    print(f'The largest number of list is - {max_of_my_list}')


if __name__ == '__main__':
    greatest_number()
