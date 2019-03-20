for asfasf in range(int(input())):
    a=int(input())
    b=[]
    d=0
    e=0
    for i in range(a):
        c=input()
        b.append(list(set([j for j in c])))
    for i in range(len(b[0])):
        d=0
        for j in range(1,a):
            #print(b[0][i],b[j],d,e)
            if b[0][i] in b[j]:
                d+=1
            else:
                break
        if(d==a-1):
            e+=1

    print(e)
            
