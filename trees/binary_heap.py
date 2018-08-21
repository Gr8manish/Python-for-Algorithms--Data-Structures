class MinBinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.current_size = 0

    def insert(self,new_data):
        self.heapList.append(new_data)
        self.current_size += 1
        self.shift_up(self.current_size)

    def shift_up(self,index):
        tmp_index = index // 2
        while tmp_index > 0:
            if self.heapList[index] < self.heapList[tmp_index]:
                self.heapList[index],self.heapList[tmp_index] = self.heapList[tmp_index],self.heapList[index]
            index = tmp_index
            tmp_index = index // 2

    def get_min(self):
        return self.heapList[1] if self.current_size > 1 else None

    def delete_min(self):
        self.heapList[1] = self.heapList[self.current_size]
        self.current_size -= 1
        self.heapList.pop()
        self.shift_down(1)

    def shift_down(self, index):
        while index*2 <= self.current_size:
            min_child_index = self.get_min_child_index(index)
            if self.heapList[min_child_index] > self.heapList[index]:
                break
            self.heapList[min_child_index], self.heapList[index] = self.heapList[index], self.heapList[min_child_index]
            index = min_child_index

    def get_min_child_index(self,index):
            if index*2+1 > self.current_size:
                return index*2
            else:
                if self.heapList[index*2] < self.heapList[index*2+1]:
                    return index*2
                else:
                    return index*2+1




# Test Cases (Insert)
minBH = MinBinaryHeap()
minBH.insert(10)
minBH.insert(5)
minBH.insert(15)
minBH.insert(2)
minBH.insert(100)
minBH.insert(1)
minBH.insert(1.2)
print minBH.heapList

# Output
# [0, 1, 5, 1.2, 10, 100, 15, 2]


# Test Case 2
minBH.delete_min()
print minBH.heapList

# Output
# [0, 1.2, 5, 2, 10, 100, 15]

