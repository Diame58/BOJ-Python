score=[]

for i in range(2):
    T,F,S,P,C=map(int,input().split())
    score.append(T*6+F*3+S*2+P+C*2)
print(score[0],score[1])