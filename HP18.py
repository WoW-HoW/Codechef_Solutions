for awwwwww in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in range(a[0]):
        if(b[i]%a[1]==0 and b[i]%a[2]==0):
            c.append("c")
        elif(b[i]%a[1]==0):
            c.append("b")
        elif(b[i]%a[2]==0):
            c.append("a")
        else:
            c.append("d")
    com=c.count("c")
    bob=c.count("b")
    ali=c.count("a")
    ch="b"
    print(com,bob,ali,c)
    if(com%2!=0):
        ch="a"
    if(bob-ali==0 and ch=='a'):
        ch='a'
    elif(bob-ali==0 and ch=='b'):
        ch='b'
    elif(bob>ali):
        ch='a'
    else:
        ch='b'
    if(ch=='a'):
        print("BOB")
    else:
        print("ALICE")
