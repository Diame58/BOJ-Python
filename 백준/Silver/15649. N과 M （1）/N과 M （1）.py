import sys

N,M=map(int, input().split())
resol=[]

def backtrack(depth):
    if depth==M:
        print(' '.join(map(str, resol)))
        return
    for i in range(1, N+1):
        if i in resol:
            continue
        
        resol.append(i)
        backtrack(depth+1)
        resol.pop()
     
backtrack(0)