import sys

for line in sys.stdin:
    if not line.strip():
        continue
    N, S = map(int, line.strip().split())
    print(S // (N + 1))