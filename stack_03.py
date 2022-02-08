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

    def get_from_stack(self, e):
        try:
            for item in self._items:
                if item == e:
                    index = self._items.index(e)
                    removed_element = self._items.pop(index)
                    return removed_element
        except ValueError:
            print('No such element')


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def get_from_stack(self, e):
        try:
            for item in self._items:
                if item == e:
                    index = self._items.index(e)
                    removed_element = self._items.pop(index)
                    return removed_element
        except ValueError:
            print('No such element')


if __name__ == "__main__":
    print('______________________________________Stack_________________________________________________')
    s = Stack()
    s.push(5)
    s.push(8)
    s.push(4)
    s.push(2)
    print(s)
    print(s.get_from_stack(8))

    print('______________________________________Queue_________________________________________________')
    q = Queue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(77)
    q.enqueue(8)
    print(q)
    print(q.get_from_stack(5))
