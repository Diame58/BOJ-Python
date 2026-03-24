import sys

N,K=map(int, sys.stdin.readline().split())
resol=1

for i in range(K):
    resol=resol*(N-i)
for i in range(1,K+1):
    resol=resol//i
print(resol)