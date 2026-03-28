H,W,N,M = map(int, input().split())

rows = (H-1)//(N+1) +1
cols = (W-1)//(M+1) +1
print(rows*cols)