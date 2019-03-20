for lol in range(int(input())):
    a=[i for i in input()]
    b=list(set(a))
    c=[]
    d=0
    e=0
    for i in range(len(b)):
        c.append(a.count(b[i]))
    print(a,b,c)
    g=len(a)//len(c)
    c=list(sorted(list(set(c))))
    while(len(list(set(c)))!=1):
        c=list(sorted(c))
        c[0]+=1
        c[-1]-=1
        d+=1
    print(d)
