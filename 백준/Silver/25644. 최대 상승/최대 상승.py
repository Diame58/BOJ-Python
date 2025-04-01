import sys

input=sys.stdin.readline

N=int(input())

cost=list(map(int,input().split()))

min_cost=cost[0]
max_profit=0

for i in range(1,N):
    max_profit=max(max_profit,cost[i]-min_cost)
    min_cost=min(min_cost,cost[i])
print(max_profit)