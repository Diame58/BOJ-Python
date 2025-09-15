import sys

n,m= map(int, input().split())

num=[]

def backTracking(depth):
    if depth==m:
        print(' '.join(map(str, num)))
        return
    
    for i in range(1,n+1):
        num.append(i)
        backTracking(depth+1)
        num.pop()

backTracking(0)