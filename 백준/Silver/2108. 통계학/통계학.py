import sys

T=int(sys.stdin.readline())

num=[]
for i in range(T):
    num.append(int(sys.stdin.readline()))

num.sort()

num_mean=round(sum(num)/T)
print(num_mean)

num_median=num[T//2]
print(num_median)

mode_count={}
for i in num:
    if i in mode_count:
        mode_count[i] += 1
    else:
        mode_count[i] = 1

max_count=0
max_mode=[]

for i, freq in mode_count.items():
    if freq > max_count:
        max_count= freq
        max_mode= [i]
    elif freq== max_count:
        max_mode.append(i)

max_mode.sort()
if len(max_mode)>1:
    print(max_mode[1])
else:
    print(max_mode[0])

num_range = max(num)-min(num)
print(num_range)