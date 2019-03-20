for awwwwwwwwwwwwww in range(int(input())):
    a,b,c,d=list(map(int,input().split()))
    e=a//b
    #print(e)
    e+=a//c
    #print(e)
    if(b%c==0 or c%b==0):
        if(c>b):
            e-=2*(a//c)
     #       print(e)
        else:
            e-=2*(a//b)
      #      print(e)
    else:
        e-=2*(a//(b*c))
       # print(e)
    if(e>=d):
        print("Win")
    else:
        print("Lose")
