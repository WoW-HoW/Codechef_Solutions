a=int(input())
b=[2, 3, 5, 7 , 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
for i in range(a):
    c=int(input())
    d=0
    for j in range(len(b)-1):
        for k in range(j+1,len(b)-j-1):
            if(c==(b[j]+b[k])):
                print(b[j],b[k],b[j]+b[k])
                d=1
                break
            
    if(d==1):
        print("YES")
    else:
        print("NO")
