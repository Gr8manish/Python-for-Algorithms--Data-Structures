def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        left_arr = merge_sort(arr[0:len(arr)//2])
        right_arr = merge_sort(arr[len(arr)//2:])
        return merge(left_arr,right_arr)


def merge(left_arr, right_arr):
    i,j=(0,)*2
    result = []
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j += 1

    while i<len(left_arr):
        result.append(left_arr[i])
        i+=1

    while j<len(right_arr):
        result.append(right_arr[j])
        j+=1

    return result


# Test Case
arr = [11,2,5,4,7,6,8,1,23]
print(merge_sort(arr))

# Output
# [1, 2, 4, 5, 6, 7, 8, 11, 23]
