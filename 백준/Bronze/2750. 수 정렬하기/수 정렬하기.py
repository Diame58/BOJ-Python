N=int(input())
li=[0 for i in range(N)]
for i in range(N):
    li[i]=int(input())
li.sort()
for i in li:
    print(i)