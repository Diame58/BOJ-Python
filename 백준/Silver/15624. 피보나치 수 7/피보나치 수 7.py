import sys

input=sys.stdin.readline

N=int(input())

mod=1000000007
x,y=0,1
for i in range(2,N+1):
    x,y=y,(x+y)%mod
print(y)