import sys

N= sys.stdin.readline()
N_list=set(map(int, input().split()))

M= sys.stdin.readline()
M_list=list(map(int, input().split()))

for i in M_list:
    print(1) if i in N_list else print(0)