a=0
b=0
c=0
for a in range(0,10):
    x=a**3
    for b in range(0,10):
        y=b**3
        for c in range(0,10):
            z=c**3
            s=a*100+b*10+c
            n=x+y+z
            if s==n:
                print（s）
