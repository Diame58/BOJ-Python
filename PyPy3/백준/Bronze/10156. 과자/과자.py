# 과자 1개 가격 K, 과자개수 N, 현재가진 돈 M -> 모자란 돈
K,N,M = map(int, input().split())
a = K*N-M
if (a>0):
    print(a)
else:
    print(0)