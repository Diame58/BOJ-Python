import sys

def backtrack(index, sum):
    global resol_max
    global resol_min
    if index==N-1:
        if resol_max<sum:
            resol_max=sum
        if resol_min>sum:
            resol_min=sum
        return
    
    for i in range(4):
        temp=sum
        if operator[i]==0:
            continue
        if i==0:
            sum+=num_arr[index+1]
        elif i==1:
            sum-=num_arr[index+1]
        elif i==2:
            sum*=num_arr[index+1]
        else:
            if sum<0:
                sum=abs(sum)//num_arr[index+1]*-1
            else:
                sum//=num_arr[index+1]
                
        operator[i]-=1
        backtrack(index+1, sum)
        operator[i]+=1
        sum=temp


N=int(input())
num_arr= list(map(int, input().split()))
operator= list(map(int, input().split()))
resol_min=float('inf')
resol_max=float('-inf')
    
    
    
backtrack(0, num_arr[0])
print(resol_max)
print(resol_min)