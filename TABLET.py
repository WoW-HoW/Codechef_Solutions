for awwwwww in range(int(input())):
    a,b=list(map(int,input().split()))
    f=[]
    g=[]
    for i in range(a):
        c,d,e=(list(map(int,input().split())))
        if(e<=b):
            f.append((c*d))
            g.append(e)
    try:
        print(max(f))
    except(ValueError):
        print("no tablet")
