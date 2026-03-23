T = int(input())
for i in range(T):
    N= int(input())
    
    dict={}
    for j in range(N):
        name, score = input().split()
        dict[name] = int(score)
    max_key = max(dict, key= lambda x: dict[x])
    print(max_key)