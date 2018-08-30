def finder(arr1, arr2):
    result = 0
    for num in arr1:
        result += num
    for num in arr2:
        result -= num
    return result


print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))  # 5
print(finder([5, 5, 7, 7], [5, 7, 7]))              # 5
print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7 , 2, 1, 4, 6]))  # 5
print(finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]))  # 6
