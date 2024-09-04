import sys

N= int(sys.stdin.readline())
arr=[]
for i in range(N):
    [a,b] = map(int,sys.stdin.readline().split())
    arr.append([a,b])
arr.sort()
for i in arr:
    print(i[0],i[1])