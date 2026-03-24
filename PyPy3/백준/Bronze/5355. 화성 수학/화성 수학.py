T = int(input())
for i in range(T):
    M = list(map(str, input().split()))
    E = float(M[0])
    for j in M:
        if j == '@':
            E *= 3
        elif j == '%':
            E += 5
        elif j == '#':
            E -= 7
    print('{:.2f}'.format(E))