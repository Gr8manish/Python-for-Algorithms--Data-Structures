class Node:
    def __init__(self,data=None):
        self.data = data
        self.next_node = None


def cycle_check(node):
    a = node
    b = node
    while(b):
        a = a.next_node
        if not b.next_node:
            return False

        b = b.next_node.next_node
        if a==b:
            return True

    return False


# Testing
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c

print(cycle_check(a))

c.next_node = a
print(cycle_check(a))

# Output
# False
# True