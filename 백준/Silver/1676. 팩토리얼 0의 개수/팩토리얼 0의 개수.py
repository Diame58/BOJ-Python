N=int(input())

fac=1
count=0

for i in range(N):
    fac*=N-i

fac=str(fac)

for i in range(1,len(fac)):
    if fac[-i]=='0':
        count+=1
    else:
        break
print(count)