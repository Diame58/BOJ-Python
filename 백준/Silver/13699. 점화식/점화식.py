import sys

input=sys.stdin.readline

N = int(input())

t=[0]*(N+1)
t[0]=1

for i in range(1,N+1):
    for j in range(i):
        t[i]+=t[j]*t[i-j-1]

print(t[N])