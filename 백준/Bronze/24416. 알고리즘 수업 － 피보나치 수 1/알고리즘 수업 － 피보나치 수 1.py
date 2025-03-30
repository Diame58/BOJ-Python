import sys

input=sys.stdin.readline

n=int(input())
def fib(n):
    fibo=[0]*(n+1)
    fibo[1]=fibo[2]=1
    for i in range(3,n+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
    return fibo[n]
def fibonacci(n):
    return n-2
print(fib(n), fibonacci(n))