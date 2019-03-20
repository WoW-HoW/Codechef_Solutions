for awwwwwww in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    d=0
    e=0
    for i in range(a):
        if(b[i]>0):
            c+=1
        elif(b[i]<0):
            d+=1
        else:
            e+=1
    if(c>d):
        c+=e
    else:
        d+=e
    if(c!=0 and d!=0):
        print(max(c,d),min(c,d))
    else:
        print(max(c,d),max(c,d))
