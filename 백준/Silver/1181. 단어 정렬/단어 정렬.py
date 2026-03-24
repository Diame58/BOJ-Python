N=int(input())
li=[]
for i in range(N):
    li.append(input())

set_li=set(li)
li=list(set_li)
li.sort()
li.sort(key=len)

for i in li:
    print(i)