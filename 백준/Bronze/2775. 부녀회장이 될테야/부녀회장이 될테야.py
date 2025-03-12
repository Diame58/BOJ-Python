T=int(input())

for i in range(T):
    k=int(input())
    n=int(input())

    people = [i for i in range(1, n + 1)]
    for j in range(1,k+1):
        for l in range(1,n):
            people[l]+=people[l-1]
    print(people[-1])