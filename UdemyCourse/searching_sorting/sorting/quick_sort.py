def quick_sort_lomuto(arr, lo, hi):
    if lo < hi:
        p = partition_lomuto(arr, lo, hi)
        quick_sort_lomuto(arr, lo, p-1)
        quick_sort_lomuto(arr, p+1, hi)


def quick_sort_hoare(arr, lo, hi):
    if lo < hi:
        p = partition_hoare(arr, lo, hi)
        quick_sort_hoare(arr, lo, p-1)
        quick_sort_hoare(arr, p+1, hi)


def partition_lomuto(arr, lo, hi):
    pivot = arr[hi]
    left = lo
    for right in range(lo, hi):
        if arr[right] < pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    arr[hi], arr[left] = arr[left], arr[hi]
    return left


def partition_hoare(arr, lo, hi):
    pivot = arr[hi]
    left = lo
    right = hi-1
    while True:
        while (left + 1) <= hi and arr[left] <= pivot:
            left += 1
        while (right-1) >= 0 and arr[right] > pivot:
            right -= 1
        if left >= right:
            arr[left], arr[hi] = arr[hi], arr[left]
            return left
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right += 1


# Test Cases
arr = [2,5,4,6,7,3,1,4,12,11]
quick_sort_lomuto(arr, 0, len(arr)-1)
print(arr)

# Output
# [1, 2, 3, 4, 4, 6, 5, 7, 11, 12]

arr = [2,5,4,6,7,3,1,4,12,11]
quick_sort_hoare(arr, 0, len(arr)-1)
print(arr)

# Output
# [1, 2, 3, 4, 4, 6, 5, 7, 11, 12]
