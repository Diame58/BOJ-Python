N=int(input())
meeting=[]
cnt=0
endTime=0

for i in range(N):
    start,end=(map(int,input().split()))
    meeting.append([start,end])
meeting.sort(key=lambda x: (x[1],x[0]))

for i in range(len(meeting)):
    if meeting[i][0]>=endTime:
        endTime=meeting[i][1]
        cnt=cnt+1
print(cnt)

