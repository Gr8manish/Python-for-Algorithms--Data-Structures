import ctypes


class DynamicArray():
    """
        Dynamic Array Class which is similar to Python List class
    """

    """
        __inti__
        __len__
        __getitem__
        append
        _resize
        make_array
        
        arr = DynamicArray()
        len(arr)
        arr[1]
        arr.append[10]
         
    """

    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._array = self._get_new_array(self._capacity)

    def __len__(self):
        return self._size

    def __getitem__(self,index):
        if index > self._size or index < 0 :
            raise IndexError("Index out of bound exception")

        return self._array[index]

    def append(self,value):
        if self._capacity == self._size:
            self._array = self._increase_array_size(self._array)
        self._array[self._size] = value
        self._size += 1

    def _get_new_array(self,capacity):
        self._capacity = capacity
        """
        Create new array of specified size
        :param capacity:
        :return new array:
        """
        return (capacity * ctypes.py_object)()

    def _increase_array_size(self, array):
        new_array = self._get_new_array(self._capacity * 2)
        for i in range(self._size):
            new_array[i] = self._array[i]
        return new_array


"""
Testing the Dynamic Array functionality
"""

arr = DynamicArray()
print(len(arr))
print(arr.append(2))
print(len(arr))
print(arr.append(7))
print(arr.append("Katappa"))
print(arr.append("Menaria"))
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])