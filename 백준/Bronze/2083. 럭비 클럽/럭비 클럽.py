import sys

input=sys.stdin.readline

while True:
    a,b,c= input().split()
    b,c=int(b),int(c)
    if a=='#' and b==0 and c==0:
        break
    else:
        if b>17 or c>=80:
            print(f'{a} Senior')
        else:
            print(f'{a} Junior')