from math import gcd as bltin_gcd
def co1(a, b):
    return bltin_gcd(a, b) != 1
for awwww in range(int(input())):
    a=int(input())
    b=(list(map(int,input().split())))
    c=0
    for i in range(1,a):
        if(co1(b[0],b[i])):
           b[i]=47
           c+=1
    if(list(set(b))==[47]):
           b[0]=43
           c=1
    b=(list(map(str,b)))
    print(c)
    print(' '.join(b))
