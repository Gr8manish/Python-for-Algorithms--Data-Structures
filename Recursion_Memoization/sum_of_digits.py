def sum_func(n):
    if n==0:
        return 0

    return (n%10)+(sum_func(int(n/10)))


print(sum_func(4321))