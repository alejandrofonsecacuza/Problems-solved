t=1
while(True):
    try:
        s=list(map(int,list(input())))
        n=int(input())
        if(len(s)==0):
            break
    except:
        break
    ta = [0] * len(s)  
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            ta[i] = ta[i-1]  
        else:
            ta[i] = ta[i-1] + 1
    print(f"Case {t}:")
    t+=1
    for _ in range(n):
        l,r=map(int,input().split())
        maximum=max(l,r)
        minimum=min(l,r)
        diff=ta[maximum]==ta[minimum]
        if(diff):
            print("Yes")
        else:
            print("No")