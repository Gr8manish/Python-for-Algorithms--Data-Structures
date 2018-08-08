class Node:
    def __init__(self,data=None):
        self.data = data
        self.next_node = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # Printing all the values in linked list
    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next_node

    # insert a value at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self,data):
        tmp = self.head
        while tmp.next_node:
            tmp = tmp.next_node
        tmp.next_node = Node(data)


# Testing
sll = SinglyLinkedList()
sll.print()

sll.insert_at_beginning(1)
sll.insert_at_beginning(2)
sll.insert_at_beginning(3)
sll.print()

sll.insert_at_end(4)
sll.insert_at_end(5)
sll.insert_at_end(6)
sll.print()