K = int(input())

num_list = []
for i in range(K):
    num = int(input())
    if num != 0:
        num_list.append(num)
    else:
        if num_list:
            num_list.pop()

print(sum(num_list))