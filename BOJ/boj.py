import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

network=[[] for i in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    network[a].append(b)
    network[b].append(a)


list1=[0]*(N+1)
def DFS(warm):
    list1[warm]=1
    count=0
    for i in network[warm]:
        if not list1[i]:
            count+=1+ DFS(i)
    return count

print(DFS(1))