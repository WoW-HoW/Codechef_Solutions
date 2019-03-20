a=int(input())
for i in range(a):
    b=(input())
    c=[*map(int,[n for n in b])]
    c=sum(c)
    b=int(b)
    d=c%9
    e=9-d
    #print(c,d,e)
    #print(f,g,h)
    if(b>9 and c<5):
        print(e)
    else:
        print(min(d,e))
