value=input().split('-')
result=0

for i in value[0].split('+'):
    result+=int(i)

for i in value[1:]:
    for j in i.split('+'):
        result-=int(j)
print(result)