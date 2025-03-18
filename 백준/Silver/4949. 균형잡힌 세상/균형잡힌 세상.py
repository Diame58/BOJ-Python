import sys

while True:
    text=sys.stdin.readline().rstrip()
    stack=[]
    flag=True

    if text=='.':
        break
    else:
        for i in text:
            if i=='(' or i=='[':
                stack.append(i)
            elif i==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    flag=False
                    break
            elif i==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    flag=False
                    break
        if flag and not stack:
            print('yes')
        else:
            print('no')