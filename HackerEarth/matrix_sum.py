# You are given a N*M matrix. You need to print the sum of all the numbers in the rectangle which has (1,1) as the top left corner and (X,Y) as the bottom right corner.

# Input:
#     First line contains two integers, N and M, number of rows and number of columns in the matrix.
#     Next N lines contains M space separated integers, elements of the matrix.
#     Next line contains an integer, Q, number of queries.
#     Each query contains two space separated integers, X and Y.
#
# Output:
#     For each query, print the sum of all the numbers in the rectangle which has  as the top left corner and  as the bottom right corner.

N,M = [int(x) for x in input().split()]
ARR = []
for i in range(N):
    ARR.append([int(x) for x in input().split()])

Q = int(input())

ANS = []
for i in range(N):
    ANS.append([])
    for j in range(M):
        ANS[i].append(0)

sum = 0
for col in range(0,M):
    sum+=ARR[0][col]
    ANS[0][col] = sum

for row in range(1,N):
    sum=0
    for col in range(0,M):
        sum+=ARR[row][col]
        ANS[row][col] = ANS[row-1][col] + sum

for q in range(Q):
    x,y = [int(x) for x in input().split()]
    print(ANS[x-1][y-1])