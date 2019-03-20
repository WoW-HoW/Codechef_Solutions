for awwwwww in range(int(input())):
    a,b,c,d=input().split()
    c=int(c)
    d=int(d)
    e=["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    f=e.index(b)-e.index(a)+1
    if(f<=0):
        f+=7
    if(c<=f<=d):
        if(1>d-f>6):
            print("many")
        else:
            print(d-f)
    else:
        print("impossible")
