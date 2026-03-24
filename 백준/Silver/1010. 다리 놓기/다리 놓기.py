import sys

input=sys.stdin.readline

T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    count=1
    if N==M:
        print(count)
    else:
        for j in range(N):
            count*=(M-j)
            count//=(j+1)
        print(count)