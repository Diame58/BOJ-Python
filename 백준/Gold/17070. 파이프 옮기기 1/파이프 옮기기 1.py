import sys

def pipe():
    pipelist[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            pipelist[0][0][i] = pipelist[0][0][i - 1]
    for r in range(1, N):
        for c in range(1, N):
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                pipelist[1][r][c] = pipelist[0][r - 1][c - 1] + pipelist[1][r - 1][c - 1] + pipelist[2][r - 1][c - 1]

            if board[r][c] == 0:
                pipelist[0][r][c] = pipelist[0][r][c - 1] + pipelist[1][r][c - 1]
                pipelist[2][r][c] = pipelist[2][r - 1][c] + pipelist[1][r - 1][c]
    print(sum(pipelist[i][N - 1][N - 1] for i in range(3)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
pipelist = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
pipe()