import sys

input=sys.stdin.readline

N,K= map(int,input().split())
coin= [int(input()) for i in range(N)]
coin.reverse()
cnt=0

for i in coin:
    if K==0:
        break
    else:
        cnt+=K//i
        K%=i
print(cnt)