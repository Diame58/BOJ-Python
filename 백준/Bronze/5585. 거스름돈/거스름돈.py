Joi = [500, 100, 50, 10, 5, 1]
Taro = 1000
resol=int(input())
zandon = Taro - resol
cnt = 0
while zandon >0:
    for i in range(len(Joi)):
        if zandon>=Joi[i]:
            zandon-= Joi[i]
            cnt+=1
            break
print(cnt)