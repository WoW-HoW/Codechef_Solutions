for awwwwwwwwww in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=a[1]
    d=b.count(1)
    if((a[0]-d)<=c):
        print("YES")
    else:
        print("NO")
