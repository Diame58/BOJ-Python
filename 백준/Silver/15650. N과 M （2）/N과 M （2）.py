import sys

input=sys.stdin.readline

N,M=map(int,input().split())

spot=[]
def dfs(num):
    if len(spot)==M:
        print(' '.join(map(str,spot)))
        return

    for i in range(num, N+1):
        if i not in spot:
            spot.append(i)
            dfs(i+1)
            spot.pop()
dfs(1)