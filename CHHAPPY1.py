import time
for awwwwwww in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=list(set(b))
    c1=True
    a2=time.time()
    for i in range(len(c)):
        d=b.count(c[i])
        if(d>1):
            l=[index for index, value in enumerate(l) if value == c[i]]
            for j in range(d):
                for k in range(j+1,d):
                    if(l[j]!=l[k]):
                        c1=False
                        break
    if(c1==False):
        print("Truly Happy")
    else:
        print("Poor Chef")
        
    print(time.time()-a2)
