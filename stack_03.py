from typing import TypeAlias, Any

T_VALUE: TypeAlias = Any


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    __len__ = size

    def __str__(self):
        return str(self._items)

    def get_from_stack(self, e):
        temp_stack = Stack()
        try:
            while self.size():
                if (temp_item := self.pop()) != e:
                    temp_stack.push(temp_item)
                else:
                    break
            else:
                raise ValueError("No such value")
        finally:
            while temp_stack.size():
                self.push(temp_stack.pop())
        return temp_item


class Queue:
    def __init__(self):
        self._items: list[T_VALUE] = []

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

    def get_from_queue(self, e):
        temp_queue = Queue()
        try:
            while self.size():
                if (temp_item := self.dequeue()) != e:
                    temp_queue.enqueue(temp_item)
                else:
                    break
            else:
                raise ValueError("No such value")
        finally:
            while temp_queue.size():
                self.enqueue(temp_queue.dequeue())
        return temp_item


if __name__ == "__main__":
    # s = Stack()
    # input_value = 'hello'
    # for item in input_value:
    #     s.push(item)
    # print(s)
    # print(s.get_from_stack('h'))
    # print(s)

    # print('______________________________________Stack_________________________________________________')
    # s = Stack()
    # s.push(5)
    # s.push(8)
    # s.push(4)
    # s.push(2)
    # print(s)
    # print(s.get_from_stack(2))
    # print(s)
    # print(s.get_from_stack(77))

    # print('______________________________________Queue_________________________________________________')
    q = Queue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(77)
    q.enqueue(8)
    print(q)
    print(q.get_from_queue(5))
    print(q)
    # print(q.get_from_queue(66))
