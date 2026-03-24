import sys

input=sys.stdin.readline

num_total=[]

for i in range(2):
    num=map(int,input().split())
    num_total.append(sum(num))
print(max(num_total))