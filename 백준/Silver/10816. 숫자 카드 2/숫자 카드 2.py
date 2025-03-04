import sys

N = int(sys.stdin.readline())
N_card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_card = list(map(int, sys.stdin.readline().split()))

count = {}

for i in N_card:
    count[i] = count.get(i, 0) + 1

print(" ".join(str(count.get(i, 0)) for i in M_card))