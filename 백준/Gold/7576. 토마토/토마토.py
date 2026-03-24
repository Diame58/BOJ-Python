from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j, 0))

max_days = 0
while queue:
    x, y, days = queue.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            box[nx][ny] = 1
            queue.append((nx, ny, days + 1))
            max_days = max(max_days, days + 1)

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()

print(max_days)