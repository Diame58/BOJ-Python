markdea = input()
stack=[]
answer=0
for i in range(len(markdea)):
    if markdea[i] == '(':
        stack.append(markdea[i])
    else:
        if markdea[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer+=1
print(answer)