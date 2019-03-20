a=int(input())
for i in range(a):
    b=int(input())
    c=0
    d=[1,0,0]
    while(c<b):
        #in bit
        if(c<b):
            c=c+2
            #out bit
        if(c<b):
            d[1]+=d[0]
            d[0]=0
            c=c+8
        #out nibble
        if(c<b):
            d[2]+=d[1]
            d[1]=0
            c=c+16
        #out byte
        if(c<b):
            d[0]=d[2]*2
            d[2]=0
    print(d[0],d[1],d[2])
