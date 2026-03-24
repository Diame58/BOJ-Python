import sys

input=sys.stdin.readline

N_list=[]
for i in range(10):
    N_list.append(float(input()))

N_list.sort(reverse=True)
N_list=N_list[:9]

result=1
for i in range(9):
    prob=N_list[i]/(i+1)
    result*=prob
print(result*10**9)