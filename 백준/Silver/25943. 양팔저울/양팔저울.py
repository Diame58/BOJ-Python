n=int(input())

dol=list(map(int, input().split()))
zagal=[100,50,20,10,5,2,1]

left=dol[0]
right=dol[1]

for i in range(2,n):
    if left==right:
        left+=dol[i]
    else:
        if left>right:
            right+=dol[i]
        else:
            left+=dol[i]

bbagi=abs(left-right)
    
cnt=0
for i in zagal:
    if bbagi>=i:
        cnt+=(bbagi//i)
        bbagi%=i

print(cnt)