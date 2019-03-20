for awwwwwwwwww in range(int(input())):
    d={'':0, 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'ae': 0, 'ai': 0, 'ao': 0, 'au': 0, 'ei': 0, 'eo': 0, 'eu': 0, 'io': 0, 'iu': 0, 'ou': 0,     'aei': 0, 'aeo': 0, 'aeu': 0, 'aio': 0, 'aiu': 0, 'aou': 0, 'eio': 0, 'eiu': 0, 'eou': 0, 'iou': 0, 'aeio': 0, 'aeiu': 0, 'aeou': 0, 'aiou': 0, 'eiou': 0, 'aeiou': 0}
    n,ans=int(input()),0
    for i in range(n):
        s=input()
        ss=''
        if('a' in s):
            ss=ss+'a'
        if('e' in s):
            ss=ss+'e'
        if('i' in s):
            ss=ss+'i'
        if('o' in s):
            ss=ss+'o'
        if('u' in s):
            ss=ss+'u'
        d[ss]=d[ss]+1
        
    i=0
    dk=list(d.keys())
    while(i<len(dk)-1):
        j=i+1
        while(j<len(dk)):
            temp=dk[i]+dk[j]
            if('a' in temp and 'e' in temp and 'i' in temp and 'o' in temp and 'u' in temp):
                ans=ans+d[dk[i]]*d[dk[j]]
            j=j+1
        i=i+1
    ans=ans+int((d['aeiou']*(d['aeiou']-1))/2)
    print((str(ans)))

    
    
    
