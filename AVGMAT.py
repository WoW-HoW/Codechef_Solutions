for awwwwwwwwwwww in range(int(input())):
    a,b=list(map(int,input().split()))
    c=[]
    f=[]
    for i in range(a):
        d=[j for j in input()]
        e=[]
        for j in range(len(d)):
            e.append(d[j])
            if(d[j]=='1'):
                f.append([i+1,j+1])
        c.append(d)
    g=len(f)
    h=[]
    u=[]
    for i in range(g):
        for j in range(i+1,g):
            h.append(abs(int(f[i][0])-int(f[j][0]))+abs(int(f[i][1])-int(f[j][1])))
    for i in range(1,a+b-1):
        if(i in h):
            u.append(str(h.count(i)))
        else:
            u.append('0')
    
    print(' '.join(u))
        
