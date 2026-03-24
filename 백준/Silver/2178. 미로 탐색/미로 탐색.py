from collections import deque

N,M= map(int, input().split())

arr=[list(map(int, input())) for i in range(N)]
d=[(-1,0), (1,0), (0,-1), (0,1)]
q= deque()
q.append((0,0))

def bfs():
    while q:
        x,y=q.popleft()
        for k in range(len(d)):
            dx= x+d[k][0]
            dy= y+d[k][1]
            if 0<=dx<N and 0<=dy<M:
                if arr[dx][dy]==1:
                    arr[dx][dy]= arr[x][y]+1
                    q.append((dx,dy))
arr[0][0]=1
bfs()
print(arr[N-1][M-1])