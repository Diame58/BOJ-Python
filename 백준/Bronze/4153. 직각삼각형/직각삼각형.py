while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break

    if max(a,b,c)==a:
        a,c=c,a
    elif max(a,b,c)==b:
        b,c=c,b

    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')
