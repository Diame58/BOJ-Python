import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for i in range(N)] for i in range(H)]

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()


def BFS():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y]+1
                    queue.append((nz, nx, ny))


for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))
BFS()

cannot_complete = 0
day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                cannot_complete = 1
            day = max(day, graph[i][j][k])

if cannot_complete:
    print(-1)
else:
    print(day-1)