import sys

input=sys.stdin.readline

N,M=map(int,input().split())

N_list=list(map(int,input().split()))

bat=[0]*(N+1)
for i in range(N):
    bat[i+1]=bat[i]+N_list[i]

for _ in range(M):
    i,j=map(int,input().split())
    print(bat[j]-bat[i-1])