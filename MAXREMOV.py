for aws in range(int(input())):
    a,b=list(map(int,input().split()))
    c=[]
    l1=100001
    r1=0
    for i in range(a):
        l,r=list(map(int,input().split()))
        c.append([l,r])
        if(l<l1):
            l1=l
        if(r>r1):
            r1=r
    d=[0]*(r1)
    for i in range(a):
        l=c[i][0]
        r=c[i][1]
        for i in range(l,r):
            d[i]=d[i]+1
    f=d.count(b)
    print(d,f)
