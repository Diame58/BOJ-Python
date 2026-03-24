import sys

input=sys.stdin.readline

while True:
    string=input().rstrip()

    if string=='#':
        break
    count=0

    for i in string.lower():
        if i in 'aeiou':
            count+=1
    print(count)