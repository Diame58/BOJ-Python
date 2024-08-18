T = int(input())
for i in range(T):
    H,W,N= map(int,input().split())

    floor=N%H
    distance=N//H+1
    if floor==0:
        floor=H
        distance-=1
    print(int(floor*100 + distance))