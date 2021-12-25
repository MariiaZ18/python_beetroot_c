# Write a function that takes in two numbers from the user via input(), call the numbers a and b,
# and then returns the value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def main_m():
    number_1 = int(input('Please, enter an integer: '))
    number_2 = int(input('Please enter a second integer: '))

    try:
        result = number_1 / number_2
    except ZeroDivisionError:
        print('Impossible operation! Zero division!')
    else:
        print(f'The result of dividing a {number_1} by a {number_2} is {result}')


if __name__ == '__main__':
    main_m()
