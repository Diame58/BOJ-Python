a,b,n,w=map(int,input().split())
arr=[]
sumNum=0
for i in range(1,n+1):
    x = i
    y = n - i
    if x>=1 and y>=1:
        sumNum = a*x+b*y
        if sumNum == w:
            arr.append([x, y])

if len(arr)==0 or len(arr)>=2:
    print(-1)
else:
    print(*arr[0])
