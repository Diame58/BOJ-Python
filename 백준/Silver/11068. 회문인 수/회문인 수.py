import sys

T = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(T)]

char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

for i in arr:
    flag = False

    for j in range(2, 65):
        n = i
        re_arr = ""

        while n > 0:
            n, k = divmod(n, j)
            re_arr = char[k] + re_arr

        if re_arr == re_arr[::-1]:
            flag = True
            break

    if flag:
        print(1)
    else:
        print(0)
