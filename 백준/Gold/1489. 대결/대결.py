N = int(input())
csortA = [0 for i in range(1002)]
csortB = [0 for i in range(1002)]

Alist = [int(i) for i in input().split()]
for i in range(N):
    csortA[Alist[i]] += 1
Blist = [int(i) for i in input().split()]
for i in range(N):
    csortB[Blist[i]] += 1
cnt = 0

for i in range(1, 1001):
    while csortA[i]:
        flag = False
        for j in range(i - 1, 0, -1):
            if csortB[j]:
                flag = True
                cnt += 2
                csortA[i] -= 1
                csortB[j] -= 1
                break
        if flag == False:
            break
for i in range(1, 1001):
    while csortA[i] and csortB[i]:
        cnt += 1
        csortA[i] -= 1
        csortB[i] -= 1
print(cnt)