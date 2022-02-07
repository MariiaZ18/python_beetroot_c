# Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def reversed_m(self):
        my_list = []
        for item in self._items[::-1]:
            my_list.append(item)
        return my_list.__str__()


if __name__ == "__main__":
    s = Stack()
    s.push('say')
    s.push('hello')
    s.push('world')
    print(s)
    print(s.reversed_m())
