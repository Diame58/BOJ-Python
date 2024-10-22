import sys

if __name__ == '__main__':
    for T in range(int(sys.stdin.readline().rstrip())):
        m, n = map(int, sys.stdin.readline().rstrip().split())
        print(1)
        for i in range(m):
            if i&1:
                for j in range(n-2, -1, -1):
                    print(f'({i},{j})')
            else:
                for j in range(n-1):
                    print(f'({i},{j})')

        for i in range(m-1, -1, -1):
            print(f'({i},{n-1})')