N=int(input())
arr=list(map(int,input().split()))
S=int(input())

for i in range(N):
    if S<=0:
        break
    idx=i
    for j in range(i+1, min(N,i+1+S)):
        if arr[j]>arr[idx]:
            idx=j
    for j in range(idx, i, -1):
        arr[j],arr[j-1]=arr[j-1],arr[j]
        S-=1

    if S<=0:
        break
print(" ".join(map(str,arr)))