N = map(int, input().split())
sum=0
for i in N:
    sum+=i*i
sum=sum%10
print(sum)