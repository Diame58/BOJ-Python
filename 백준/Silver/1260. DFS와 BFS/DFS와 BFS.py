import sys
input=sys.stdin.readline

N,M,V=map(int,input().split())

graph=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

list1=[0]*(N+1)
list2=[0]*(N+1)
def DFS(V):
    list1[V]=1
    print(V, end=' ')
    for i in range(1,N+1):
        if graph[V][i]==1 and list1[i]==0:
            DFS(i)

def BFS(V):
    queue=[V]
    list2[V]=1
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1,N+1):
            if graph[V][i]==1 and list2[i]==0:
                queue.append(i)
                list2[i]=1

DFS(V)
print()
BFS(V)