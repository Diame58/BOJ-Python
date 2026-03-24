import sys
N=int(sys.stdin.readline().strip())
queue=[]

for i in range(N):
    data=sys.stdin.readline().strip().split()
    if data[0]=='push':
        queue.append(data[1])
    elif data[0]=='pop':
        if len(queue)!=0:
            print(queue.pop(0))
        else:
            print(-1)
    elif data[0]=='size':
        print(len(queue))
    elif data[0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif data[0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif data[0]=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
