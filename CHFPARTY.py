for awwwww in range(int(input())):
    a=int(input())
    b=list(sorted(list(map(int,input().split()))))
    c=0
    d=0
    for i in range(a):
        if(d>=b[i]):
            c+=b[i]
            d+=1
    print(d)
