import timeit
a,b=[*map(int,input().split())]
c=[*map(int,input().split())]
d=[*map(int,input().split())]
e=[0]*a
#print(c,d)
sttart_time = timeit.default_timer()
for i in range(b+1):
    for i in range(a):
        e[i]=c[i]*d[i]
    #print(e)
    c[e.index(max(e))]-=1
    #print(max(e))
print(max(e))
print(timeit.default_timer()-sttart_time)
