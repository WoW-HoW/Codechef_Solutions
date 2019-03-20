for awwwwww in range(int(input())):
    a1=input()
    a=[i for i in a1]
    a=[0]+list(map(int,a))
    b=[0,1,2,3,4,5,6,7,8,9]
    c=int(a1)
    d=c
    for i in range(len(a)-1,0,-1):
        print(a[i],a[i-1])
        if(a[i]<=a[i-1]):
            a[i]=9
        elif(d>c):
            a[i]-=1
        d=int(''.join(list(map(str,(a)))))
        print(a,d)
    
