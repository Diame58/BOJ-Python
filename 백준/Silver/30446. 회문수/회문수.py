import sys

n=int(input())

pal=set()

i=1

while True:
    half=str(i)
    
    even_pal_str=half+half[::-1]
    even_pal=int(even_pal_str)
    
    odd_pal_str=half+half[:-1][::-1]
    odd_pal=int(odd_pal_str)
    
    if odd_pal<=n:
        pal.add(odd_pal)
    if even_pal<=n:
        pal.add(even_pal)
    
    if odd_pal>n and even_pal>n:
        break
    
    i+=1
print(len(pal))