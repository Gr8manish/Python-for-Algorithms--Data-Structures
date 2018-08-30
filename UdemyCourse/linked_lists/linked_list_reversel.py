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

    def __reversed__(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next
        self.head = prev



# Testing
sll = SinglyLinkedList()
sll.print()

sll.insert_at_beginning(1)
sll.insert_at_beginning(2)
sll.insert_at_beginning(3)
sll.print()

print("**************")
reversed(sll)
sll.print()