docu = input()
voca = input()
voca_len = len(voca)
cnt=0

while len(docu) >= voca_len:
    if docu[:voca_len] == voca:
        docu= docu[voca_len:]
        cnt+=1
    else:
        docu=docu[1:]
print(cnt)