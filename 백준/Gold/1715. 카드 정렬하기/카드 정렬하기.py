import heapq
n=int(input())

arr=list(int(input()) for i in range(n))
heapq.heapify(arr)
result=0

while len(arr)!=1:
    min1=heapq.heappop(arr)
    min2=heapq.heappop(arr)
    sum=min1+min2
    result+=sum
    heapq.heappush(arr,sum)
print(result)
