K,N=map(int,input().split())

num=[]
for i in range(K):
    num.append(int(input()))

start=1
end=max(num)

result=0
while start<=end:
    mid=(start+end)//2
    count=0

    for i in num:
        count+=i//mid

    if count>=N:
        result=mid
        start=mid+1
    else:
        end=mid-1
print(result)