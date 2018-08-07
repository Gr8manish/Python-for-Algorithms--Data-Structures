class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop();

    def size(self):
        return len(self.items)


# Test Cases
q = Queue()
print(q.size())
q.isEmpty()
q.enqueue(1)
print(q.dequeue())