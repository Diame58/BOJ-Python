T=int(input())

for i in range(T):
    N=int(input())
    zero,one=1,0
    for j in range(N):
        zero,one=one,zero+one
    print(zero,one)