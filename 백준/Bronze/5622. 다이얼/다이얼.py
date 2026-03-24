A=input()
dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
b=0
for i in range(len(A)):
    for j in dial:
        if A[i] in j:
            b+=dial.index(j)+3
print(b)