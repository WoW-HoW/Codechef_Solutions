a=input()
b=int(input())
def reverse(string): 
    string = "".join(reversed(string)) 
    return string
for i in range(b):
    c,d,e,f=[*map(int,input().split())]
    c-=1
    d-=1
    e-=1
    f-=1
    g=reverse(a[c:d+1])
    #print(g)
    h=a[:c]+g+a[d+1:]
    #print(h[e:f+1])
    if(reverse(h[e:f+1])==h[e:f+1]):
        print("Yes")
    else:
        print("No")
