def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [3,5,2,7,6,8,12,40,21]
print(selection_sort(arr))
