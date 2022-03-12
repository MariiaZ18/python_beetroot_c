class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, newnext):
        self.next = newnext

    def get_data(self):
        return self.value


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            current = current.next
            return False

    def remove(self, item):
        current = self.head
        previous = None

        while True:
            if current.value == item:
                break
            previous, current = current, current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def insert(self, index, newdata):
        current = self.head
        for i in range(index):
            current = current.get_next()
        if current != None:
            temp = Node(newdata)
            temp.set_next(current.get_next())
            current.set_next(temp)
        else:
            raise ("index out of range")

    def __repr__(self):
        result = "["
        node = self.head
        if node != None:
            result += str(node.value)
            node = node.next
            while node:
                result += ", " + str(node.value)
                node = node.next
        result += "]"
        return result

    def pop(self):
        current = self.head
        previous = None

        if current == None:
            return "No item in list"

        while current.get_next() != None:
            previous = current
            current = current.get_next()

        previous.set_next(None)
        return current.get_data()


new_list = UnorderedList()
new_list.append(1)
new_list.append(2)
new_list.append(3)
new_list.append(5)
new_list.append(6)
new_list.append(7)
new_list.append(8)
print(new_list.search(8))
new_list.insert(0, 4)
print(new_list)
new_list.pop()
print(new_list)
new_list.remove(5)
print(new_list)
