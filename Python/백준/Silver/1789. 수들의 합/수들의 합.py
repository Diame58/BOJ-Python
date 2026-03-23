# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
S = int(input())
total = 0
N = 0
while True:
    N += 1
    if total + N > S:
        break
    total += N
print(N - 1)