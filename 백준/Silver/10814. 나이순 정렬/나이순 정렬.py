import sys

N= int(sys.stdin.readline())
arr=[]
for i in range(N):
    age,name =input().split()
    arr.append([int(age),name])
arr.sort(key=lambda x: int(x[0]))
for i in arr:
    print(i[0],i[1])