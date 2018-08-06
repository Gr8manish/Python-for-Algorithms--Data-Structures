# Given an integer array, output all the unique pairs that sum up to a specific value k.

def pair_sum(arr,k):
    seen = set()
    output = set()

    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target,num),max(target,num)))

    return len(output)


# Test Cases
print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum([1,2,3,1],3))
print(pair_sum([1,3,2,2],4))