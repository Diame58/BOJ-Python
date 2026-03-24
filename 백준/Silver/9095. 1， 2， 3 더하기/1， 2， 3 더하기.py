import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

T=int(input())

df=[0]*11
for _ in range(T):
    N=int(input())

    df[1]=1
    df[2]=2
    df[3]=4
    for i in range(4,N+1):
        df[i]=df[i-1]+df[i-2]+df[i-3]
    print(df[N])
