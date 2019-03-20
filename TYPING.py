for aww in range(int(input())):
    a=int(input())
    b=[]
    for i in range(a):
        b.append(input())
    l=['d','f']
    r=['j','k']
    c=[]
    d=0
    e=[]
    f=0
    for i in range(a):
        if b[i] not in c:
            d+=2
            f=d            
            for j in range(1,len(b[i])): 
                if((b[i][j-1]==l[0] and b[i][j]==l[1]) or (b[i][j-1]==l[1] and b[i][j]==l[1]) or (b[i][j-1]==l[0] and b[i][j]==l[0]) or (b[i][j-1]==r[0] and b[i][j]==r[0]) or (b[i][j-1]==r[1] and b[i][j]==r[1]) or (b[i][j-1]==l[1] and b[i][j]==l[0]) or (b[i][j-1]==r[0] and b[i][j]==r[1]) or (b[i][j-1]==r[1] and b[i][j]==r[0])):
                    d+=4
                else:
                    d+=2            
        else:
            f=d+2
            d+=e[c.index(b[i])]//2
        c.append(b[i])
        e.append(d-f+2)

    print(d)
