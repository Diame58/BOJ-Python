T=int(input())
stair=[int(input()) for i in range(T)]
dp=[0]*T


if len(stair)<=2:
    print(sum(stair))    
else:
    dp[0]=stair[0]
    dp[1]=stair[0]+stair[1]
    dp[2]=max(stair[0]+stair[2], stair[1]+stair[2])
    for i in range(3,T):
        dp[i]=max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i])
    print(dp[-1])