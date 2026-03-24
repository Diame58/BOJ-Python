import sys
input=sys.stdin.readline

N,M=map(int,input().split())

poket_monster={}
for i in range(1,N+1):
    name=input().rstrip()
    poket_monster[name]=i
    poket_monster[i]=name

for i in range(M):
    poket=input().rstrip()
    if poket.isdigit():
        print(poket_monster[int(poket)])
    else:
        print(poket_monster[poket])