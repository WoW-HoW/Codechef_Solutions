a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    d=0
    e=0
    t=0
    m=0
    while(True):
        #print(t,d,b,e,c[d-t:d+1])
        m=sum(c[d-t:d+1])
        d+=m
        e+=1
        t=d
        if(d>=b-1):
            break
    print(e)

