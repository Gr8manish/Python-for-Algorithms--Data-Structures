def insertion_sort(arr):
    for i in range(len(arr)):
        ele_value = arr[i]
        insert_at = i
        for j in range(i-1,-1,-1):
            if arr[j] < ele_value:
                break
            insert_at -= 1
            arr[j+1] = arr[j]
        arr[insert_at] = ele_value
    return arr


# Test Cases
arr =[3,5,4,6,8,1,2,12,41,25]
print(insertion_sort(arr))