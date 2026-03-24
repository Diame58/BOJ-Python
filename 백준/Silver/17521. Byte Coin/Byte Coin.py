
n,W= map(int, input().split())

coin=[int(input()) for i in range(n)]

coin_num=0
cash=W

for i in range(n-1):
    today_cost=coin[i]
    tomorrow_cost=coin[i+1]
    
    if today_cost<tomorrow_cost:
        buy_count=cash//today_cost
        coin_num+=buy_count
        cash-=buy_count*today_cost
        
    elif today_cost>tomorrow_cost:
        cash+=coin_num*today_cost
        coin_num=0
        
cash+=coin_num*coin[n-1]

print(cash)