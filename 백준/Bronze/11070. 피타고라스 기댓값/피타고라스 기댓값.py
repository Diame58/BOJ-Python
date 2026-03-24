T= int(input())

for i in range(T):
    n,m=map(int,input().split())
    plus,minus=[0]*n,[0]*n

    for j in range(m):
        a,b,p,q=map(int,input().split())
        plus[a-1]+=p
        minus[a-1]+=q
        plus[b-1]+=q
        minus[b-1]+=p
    resol=[]
    for j in range(n):
        if plus[j]**2+minus[j]**2!=0:
            resol.append(plus[j]**2/(plus[j]**2+minus[j]**2))
        else:
            resol.append(0)
    print(int(max(resol)*1000))
    print(int(min(resol)*1000))