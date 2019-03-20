for awwww in range(int(input())):
    a,b=input().split()
    a=[i for i in a]
    c=len(a)
    f=[]
    while(True):
        d=min(a)
        if(d<b):
            f.append(d)
        a=a[a.index(d)+1:]
        #print(f,a)
        if(len(list(set(a)))==0):
            break
    f+=[b]*(c-len(f))
    print(''.join(f))
