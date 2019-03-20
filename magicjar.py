for awwww in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=b[0]
    for i in range(1,a):
        c+=b[i]-1
    print(c)
