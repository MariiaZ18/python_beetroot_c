# Write a Python program to detect the number of local variables declared in a function.

def loc_var():
    a1 = 7
    str1 = 'Hello'
    char1 = 'd'
    a2 = 58


print(f'Number of local variables: {loc_var.__code__.co_nlocals}')
