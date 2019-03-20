for awwwwwwwww in range(int(input())):
    a,b=[*map(int,input().split())]
    c=list(map(int,input().split()))
    d=len(c)
    e=[]
    l=[]
    z=[]
    y=0
    for i in range(d):
        for j in range(i+1,d+1):
            e.append(c[i:j])
    l=e.copy()
    for i in range(len(e)):
        f=len(e[i])
        if(f==0):
            print(0)
            break
        else:
            w=len(l[i])
            if(b/f==b//f):
                m=b//f
            else:
                m=(b//f)+1
            e[i]=list(sorted(e[i]*m))
            g=l[i][w-1]
            h=l[i].count(g)
            if(str(h) in l[i]):
                y+=1
    if(f!=0):
        print(y)
