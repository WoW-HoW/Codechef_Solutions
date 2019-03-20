for awwwwwww in range(int(input())):
    a=list(map(int,input().split()))
    a,b,c=list(map(bin,a))
    a=a[2:]
    b=b[2:]
    c=c[2:]
    print(a,b,c)
    
