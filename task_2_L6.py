# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

def phone_number():
    number = input("Enter the number: ")

    if len(number) == 10 and number.isdigit():
        s = f'The {number} is phone number'
        return s
    else:
        l = f'The {number} is not phone number'
        return l


if __name__ == '__main__':
    print(phone_number())

# num = int(input("Give me some int pls: "))
# print(num)
# print(type(num))
# if type(num == int):
# print('Thank you')
