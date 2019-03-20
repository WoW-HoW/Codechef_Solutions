a=int(input())
for i in range(a):
    b=int(input())
    f={}
    d1=0
    for j in range(b-1):
        d,e=[*map(int,input().split())]
        try:
            f[d].append(e)
        except(KeyError):
            f[d]=[]
            f[d].append(e)
    
    for k in list(f.keys()):
        if(len(f[k])>=2):
            d1+=1
    if(b>=2):
           print("YES")
    else:
           print("NO")
