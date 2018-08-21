# Using Memoization to store results


memoization_dict = {}

def fibonacci_dynamic(n):
    if n == 2:
        return [0,1]
    if memoization_dict.get(n):
        print(f"{n} in memoization array")
        return memoization_dict[n]

    temp = fibonacci_dynamic(n-1)
    temp.append(temp[n-2]+temp[n-3])
    memoization_dict[n] = temp
    return temp


print(fibonacci_dynamic(10))

# For this input, first 10 element will be available in memoization_dict
print(fibonacci_dynamic(15))

# ******** Output *****************
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# 10 in memoization array
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
