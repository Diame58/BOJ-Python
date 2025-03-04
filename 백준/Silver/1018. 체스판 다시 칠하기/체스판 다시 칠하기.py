import sys

N, M = map(int, sys.stdin.readline().split())

if not (8 <= N <= 50 and 8 <= M <= 50):
    raise ValueError("N, M은 8 이상 50 이하")

board = [input().strip()[:M] for i in range(N)]

pat1 = ["WBWBWBWB", "BWBWBWBW"] * 4
pat2 = ["BWBWBWBW", "WBWBWBWB"] * 4

min_repaints = float('inf')

for x in range(N - 7):
    for y in range(M - 7):
        count1, count2 = 0, 0

        for i in range(8):
            for j in range(8):
                if board[x + i][y + j] != pat1[i][j]:
                    count1 += 1
                if board[x + i][y + j] != pat2[i][j]:
                    count2 += 1

        min_repaints = min(min_repaints, count1, count2)
print(min_repaints)