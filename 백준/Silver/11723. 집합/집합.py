import sys

input=sys.stdin.readline

M= int(input())
S= set()

for i in range(M):
    command= input().strip()
    if " " in command:
        com,num= command.split()
        num= int(num)
    else:
        com= command

    if com== 'add':
        S.add(num)
    elif com== 'remove':
        S.discard(num)
    elif com== 'check':
        print(1 if num in S else 0)
    elif com== 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif com== 'all':
        S = set(range(1, 21))
    elif com== 'empty':
        S.clear()