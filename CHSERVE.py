a=int(input())
for i in range(a):
    b,c,d=[*map(int,input().split())]
    e=b+c
    f=e//d
    if(f%2==0):
        print("CHEF")
    else:
        print("COOK")
