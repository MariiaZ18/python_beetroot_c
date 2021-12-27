# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)

import random


def main():
    string = list(input("Please, enter one word: "))
    string_1 = []
    string_2 = []
    n = 0
    k = len(string)
    while n <= k:
        for i in range((len(string))):
            string_1.append(string[i])
        for j in range(len(string)):
            a = random.sample(string_1, len(string))
            string_2.append(str("".join(a)))
        n += 1
        return string_2
        break


if __name__ == '__main__':
    print(main())
