import sys

input=sys.stdin.readline

m,n=map(int,input().split())
matrix=[list(map(int, input().split())) for i in range(m)]

prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

cnt = 0

for r1 in range(1, m + 1):
    for c1 in range(1, n + 1):
        for r2 in range(r1, m + 1):
            for c2 in range(c1, n + 1):
                rectan_sum = prefix_sum[r2][c2] - prefix_sum[r1 - 1][c2] - prefix_sum[r2][c1 - 1] + prefix_sum[r1 - 1][c1 - 1]

                if rectan_sum == 10:
                    cnt += 1
                if rectan_sum > 10:
                    break

print(cnt)