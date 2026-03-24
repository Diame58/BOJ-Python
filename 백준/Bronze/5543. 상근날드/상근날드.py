import sys

input=sys.stdin.readline

burger=[]
for i in range(3):
    burger.append(int(input()))
beverage=[]
for i in range(2):
    beverage.append(int(input()))
print(min(burger)+min(beverage)-50)