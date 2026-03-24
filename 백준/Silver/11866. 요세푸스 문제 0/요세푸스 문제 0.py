import sys

N,K=map(int, sys.stdin.readline().split())

idx=0
N_list=[i for i in range(1,N+1)]
resol=[]

while N_list:
    idx += K-1
    if idx >=len(N_list):
        idx %= len(N_list)
    resol.append(str(N_list.pop(idx)))
print('<',', '.join(resol),'>', sep="")