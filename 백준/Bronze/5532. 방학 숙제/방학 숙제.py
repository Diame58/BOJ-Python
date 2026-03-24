import sys

input=sys.stdin.readline

L= int(input())
A= int(input())
B= int(input())
C= int(input())
D= int(input())

korean=A//C
math=B//D

if korean>math:
    if A%C==0:
        print(L-korean)
    else:
        print(L-1-korean)
else:
    if B%D==0:
        print(L-math)
    else:
        print(L-1-math)