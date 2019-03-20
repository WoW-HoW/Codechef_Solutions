import time
for awwwwwww in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=list(set(b))
    c1=True
    a2=time.time()
    l=[]
    for i in range(len(c)):
        d=b.count(c[i])
        e=b.index(c[i])
        if(d>1):
            for j in range(a):
                for k in range(b.index(c[i]),a):
                    if(b[j]!=b[k]):
                        if(b[b[j]-1]==b[b[k]-1]):

                            c1=False
                            break
    if(c1==False):
        print("Truly Happy")
    else:
        print("Poor Chef")
        
    print(time.time()-a2)
