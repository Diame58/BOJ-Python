import sys

input=sys.stdin.readline

N=int(input())
P=list(map(int,input().split()))
count=0
sum=0
P.sort()
for i in range(N):
    sum+=P[i]
    count+=sum
print(count)