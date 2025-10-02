n=int(input())

container=list(map(int, input().split()))

con_avg=sum(container)//n

cnt_over=0
cnt_under=0

for i in container:
    if i>con_avg+1:
        cnt_over+=i-con_avg-1
    elif i<con_avg:
        cnt_under+=con_avg-i

print(max(cnt_over, cnt_under))