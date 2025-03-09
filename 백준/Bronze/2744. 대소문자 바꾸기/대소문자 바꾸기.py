text=input()

change_text=[]
for i in text:
    if i.isupper()==1:
        change_text.append(i.lower())
    else:
        change_text.append(i.upper())
print(''.join(change_text))