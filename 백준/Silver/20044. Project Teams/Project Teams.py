n=int(input())

coding=list(map(int, input().split()))

coding.sort()

sm=1000000000
for i in range(2*n):
    if sm>coding[i]+coding[2*n-1-i]:
        sm=coding[i]+coding[2*n-1-i]

print(sm)