N=str(input())
flag = False
sumNum=0
for i in range(int(N)):
    sumNum=int(i)
    strI = str(i)
    for j in range(len(strI)):
        sumNum+=int(strI[j])
    if sumNum==int(N):
        print(i)
        flag = True
        break
if flag == False:
    print(0)
