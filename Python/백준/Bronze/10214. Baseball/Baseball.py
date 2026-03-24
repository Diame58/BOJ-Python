# 연세대 득점 Y와 고려대 득점 K가 공백으로 구분되어 주어진다. 

T = int(input())
for i in range(T):
    Y=0
    K=0
    for j in range(9):
        a,b = map(int, input().split())
        Y+=a
        K+=b
    if Y>K:
        print('Yonsei')
    elif Y<K:
        print('Korea')
    else:
        print('Draw')