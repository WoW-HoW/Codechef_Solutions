a=int(input())
b=int(input())
c=[]
d=0
for i in range(b):
    c.append(int(input()))
for i in range(b):
    if(c[i]==a):
        d=1
if(d==1):
    print('FOUND')
else:
    print("NOT FOUND")
