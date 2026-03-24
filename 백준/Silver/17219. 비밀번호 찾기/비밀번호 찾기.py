N,M=map(int,input().split())

site={}
for i in range(N):
    address, password=input().split()
    site[address]=password

for i in range(M):
    find_site=input()
    print(site[find_site])