# https://www.codechef.com/SEPT18B/problems/CHEFADV

test_cases = int(input())
while test_cases != 0:
    M,N,X,Y = [int(x) for x in input().rstrip().split()]
    M-=1
    N-=1

    if M%X==0 and N%Y==0:
        print("Chefirnemo")
    elif (M>=1 and N>=1) and (M-1)%X==0 and (N-1)%Y==0:
        print("Chefirnemo")
    else:
        print("Pofik")

    test_cases-=1