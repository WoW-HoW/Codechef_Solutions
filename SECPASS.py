for awwwwwwww in range(int(input())):
    a=int(input())
    b=input()
    c=0
    e=b[0]
    c=b.count(e)
    for i in range(1,(a//c)):
        e=e+b[i]
        d=b.count(e)
        #print(d)
        if(d==c):
            c=d
        else:
            e=e[:-1]
            break
    print(e)
