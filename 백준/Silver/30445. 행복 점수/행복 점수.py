import sys

message = sys.stdin.readline().strip()
happy = 'HAPPY'
sad = "SAD"
PH = 0
PG = 0

for i in message:
    if i in happy:
        PH += 1
    if i in sad:
        PG += 1
        
if PH + PG == 0:
    print('50.00')
else:
    H = PH / (PH + PG)
    resol=H*100
    
    print(f'{resol+ 1e-9:.2f}')