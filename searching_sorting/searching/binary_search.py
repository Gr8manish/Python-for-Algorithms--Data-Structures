def binary_search(arr, ele):
    if arr is None or len(arr) == 0:
        return False
    if len(arr) == 1:
        return arr[0] == ele

    mid = len(arr)//2
    if arr[mid] == ele:
        return True
    else:
        if ele < arr[mid]:
            return binary_search(arr[0:mid], ele)
        else:
            return binary_search(arr[mid+1:], ele)


# Test Cases
arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr, 3))
print(binary_search(arr, 11))

# Output
# True
# False
