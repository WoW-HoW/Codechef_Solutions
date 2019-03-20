a=int(input())
def pri(x):
    f=0
    for i1 in range(2,int(x**0.5)+1):
        if(x%i1==0):
            f=1
            break
    return f
for i in range(a):
    b,c=list(map(int,input().split()))
    for j in range(b,c+1):
        if(pri(j)==0 and j>1):
            print(j)
