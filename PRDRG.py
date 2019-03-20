a=list(map(int,input().split()))
b=1/2
c=1/2
d=[1/2]
for i in range(2,max(a)+1):
    if(i%2==0):
        c=c/2
        b-=c
        d.append((b))
    else:
        c=c/2
        b+=c
        d.append((b))
for i in a[1:]:
    print(str(((d[i-1]).as_integer_ratio())[0])+' '+str(((d[i-1]).as_integer_ratio())[1]),end=" ")
