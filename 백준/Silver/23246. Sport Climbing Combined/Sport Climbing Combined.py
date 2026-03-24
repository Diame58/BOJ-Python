n=int(input())


resol=[]

num,a,b,c=0,0,0,0
for i in range(n):
    num,a,b,c= map(int,input().split())
    gob=a*b*c
    hab=a+b+c
    resol.append((gob,hab,num))
resol.sort(key=lambda x:(x[0],x[1],x[2]))
print(resol[0][2], resol[1][2], resol[2][2])