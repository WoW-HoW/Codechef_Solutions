a=int(input())
for i in range(a):
    b=(input())
    n=b[20:]
    #print(n)
    d=0
    e=0
    f=0
    m=[]
    c=[*map(int,[n for n in b])]
    for j in range(0,20):
        if(c[j]==1):
            d+=1
        else:
            e+=1
        if(d==11):
            print("WIN")
            break
        if(e==11):
            print("LOSE")
            break
        if(d==e==10):
            f=1
            break
    #print(f)
    if(f==1):
        for k in range(0,len(n)):
            if(n[k]+n[k+1]=='00'):
                print("LOSE")
                break
            if(n[k]+n[k+1]=='11'):
                print("WIN")
                break
