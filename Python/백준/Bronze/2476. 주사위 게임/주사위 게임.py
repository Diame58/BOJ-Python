# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  

N = int(input())
resol = 0
for i in range(N):
    a, b, c = map(int, input().split())
    li = [a, b, c]
    li.sort()
    money = 0
    if a == b == c:
        money += 10000 + a * 1000
    elif len(set(li)) == 2:
        if a == b:
            same = a
        elif b == c:
            same = b
        elif a==c:
            same = c
        money += 1000 + same * 100
    else:
        money += li[2] * 100
    if resol < money:
        resol = money
print(resol)