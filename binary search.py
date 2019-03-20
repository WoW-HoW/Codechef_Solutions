a=int(input())# to be found
b=int(input())#len
c=[*map(int,input().split())]
d=0
c=sorted(c)
print(c)
e=0
f=b
h=1
g=b+1
while(e<=f):
    if(g==(f+e)//2):
        break
    g=e+((f-e)//2)
    print(g)
    if(c[g]>a):
        f=g
    elif(c[g]<a):
        e=g
    else:
        print("found")
        h=0
        break
if(h!=0):
    print("NOT FOUND")
