for awwwwwwwwww in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=[]
    e=[]
    for i in range(a-1):
        d.append(b[i+1]+b[i-1])
    d.append(b[-2]+b[0])
    #print(d)
    for i in range(a):
        if(d[i]<c[i]):
            e.append(c[i])
    if(len(e)>0):
        print(max(e))
    else:
        print('-1')
