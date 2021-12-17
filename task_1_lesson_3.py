# Task 1
# The greeting program.
# Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:
# “Good day <name>! <day> is a perfect day to learn some python.”
# Note that <name> and <day> are predefined variables in source code.
# An additional bonus will be to use different string formatting methods for constructing result string.

name = 'Mariia'
day = 'Friday'

print(f'\n1 Good day {name}! {day} is a perfect day to learn some python.')

s = '\n2 Good day {}! {} is a perfect day to learn some python.'
print(s.format(name, day))

print('\n3 Good day {}! {} is a perfect day to learn some python'.format(name, day))

print('\n4 Good day' + ' Mariia' + '!' + ' Friday' + ' is a perfect day' + ' to learn some' + ' python\n')

l = 'Good day Mariia! Friday is a perfect day to learn some python'
print('Length of "Good day Mariia! Friday is a perfect day to learn some python" is -', len(l))
print('\n')

l = l.replace('Mariia', 'Yulia')
print(l)
