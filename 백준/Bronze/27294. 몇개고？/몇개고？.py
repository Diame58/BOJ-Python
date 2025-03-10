T,S= map(int,input().split())

if S==1 or T not in range(12,17):
    print(280)
if T in range(12,17) and S==0:
    print(320)