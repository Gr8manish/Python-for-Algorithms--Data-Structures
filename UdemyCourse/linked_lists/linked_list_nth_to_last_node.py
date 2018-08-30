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

    def nth_to_last_node(self,index):
        tmp = self.head
        len = 0
        while tmp:
            tmp = tmp.next_node
            len+=1

        count = len -index+1
        tmp = self.head
        while tmp:
            count-=1
            if count==0:
                return tmp.data
            tmp = tmp.next_node

        return None


# Testing
sll = SinglyLinkedList()
sll.print()

sll.insert_at_beginning(1)
sll.insert_at_beginning(2)
sll.insert_at_beginning(3)
sll.print()

print("**************")
print(sll.nth_to_last_node(2))