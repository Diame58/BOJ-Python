import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    bat[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and bat[ny][nx] == 1:
            dfs(nx, ny)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    bat = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        bat[y][x] = 1

    worm_count = 0

    for y in range(N):
        for x in range(M):
            if bat[y][x] == 1:
                dfs(x, y)
                worm_count += 1

    print(worm_count)