# Implement a stack using singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack_L_L:
    def __init__(self):
        self.head = None

    def get_data(self):
        return self.data

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head == None:
            return None
        else:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            return pop_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def __repr__(self):
        result = "["
        node = self.head
        if node != None:
            result += str(node.data)
            node = node.next
            while node:
                result += ", " + str(node.data)
                node = node.next
        result += "]"
        return result


s = Stack_L_L()
s.push(11)
s.push(22)
s.push(33)
s.push(44)
print(s)
print("\nTop: ", s.peek())
s.pop()
s.pop()
