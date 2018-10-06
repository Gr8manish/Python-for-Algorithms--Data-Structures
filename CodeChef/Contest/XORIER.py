# https://www.codechef.com/SEPT18B/problems/XORIER

test_cases = int(input())

while test_cases!=0:
    # For each test case
    N = int(input())
    ARR = [int(x) for x in input().rstrip().split()]

    # Magic starts here
    EVEN = []
    ODD = []

    # Assign value to EVEN,ODD and dict
    for val in ARR:
        if val%2==0:
            EVEN.append(val)
        else:
            ODD.append(val)


    EVEN = sorted(EVEN)
    ODD = sorted(ODD)

    # Lets find all combinations and find ans
    ans = 0
    length = len(ODD)
    dp = {}
    for i in range(length):
        if dp.get(ODD[i]):
            ans += dp[ODD[i]]
            continue
        for j in range(i+1,length):
            if ODD[i] ^ ODD[j] >3:
                ans += length - j
                dp[ODD[i]] = length - j
                break

    length = len(EVEN)
    dp = {}
    for i in range(length):
        if dp.get(EVEN[i]):
            ans += dp[EVEN[i]]
            continue
        for j in range(i + 1, length):
            if EVEN[i] ^ EVEN[j] > 3:
                ans += length - j
                dp[EVEN[i]] = length - j
                break

    print(ans)
    test_cases -= 1