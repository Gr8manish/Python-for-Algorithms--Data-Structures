# https://www.codechef.com/SEPT18B/problems/MAGICHF

testcases = int(input())

while testcases!=0:

    N , X , S = [int(x) for x in input().rstrip().split()]
    while S != 0:
        a,b = [int(x) for x in input().rstrip().split()]
        if a == X:
            X = b
        elif (b == X):
            X = a
        S -= 1
    print(X)

    testcases -= 1