import sys

N=int(sys.stdin.readline())

colorpaper=[list(map(int,sys.stdin.readline().split())) for i in range(N)]

white=0
blue=0

def divideandconquer(x,y,N):
    global white,blue
    samecolor=colorpaper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if samecolor!=colorpaper[i][j]:
                divideandconquer(x,y,N//2)
                divideandconquer(x,y+N//2,N//2)
                divideandconquer(x+N//2,y,N//2)
                divideandconquer(x+N//2,y+N//2,N//2)
                return
    if samecolor==0:
        white+=1
        return
    else:
        blue+=1
        return
divideandconquer(0,0,N)
print(white)
print(blue)