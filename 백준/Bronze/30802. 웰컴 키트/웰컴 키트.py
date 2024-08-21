N=int(input())
arr=list(map(int,input().split()))
T,P=map(int,input().split())
Tsum=0
for i in arr:
    if i==0:
        continue
    elif i<=T:
        Tsum+=1
    elif i%T==0:
        Tsum+=i//T
    else:
        Tsum+=i//T+1
Psum=N//P
Prest=N%P
print(Tsum)
print(f'{Psum} {Prest}')