# String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
# Sample String: 'helloworld'
# Expected Result : 'held'
# Sample String: 'my'
# Expected Result : 'mymy'
# Sample String: ' x'
# Expected Result: Empty String

def string_manipulation(my_string: str) -> str:
    if len(my_string) == 2:
        my_string *= 2
        return my_string

    elif len(my_string) >= 2:
        line = f'{my_string[0:2]}' + f'{my_string[-2:]}'
        return line

    else:
        return ''


if __name__ == '__main__':
    print(string_manipulation('ho'))
