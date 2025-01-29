from collections import defaultdict
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    s=list(input())
    band=False
    dot=True
    for i in s:
        if(i=="p" or i=="s"):
            dot=False
    if(dot):
        return "YES"

    for i in s:
        if(i=="p"):
            band=True
        if(band and i=="s"):
            return "NO"
    counter=defaultdict(int)
    for i in s:
        counter[i]+=1
    
    if(counter["s"]==0 or counter["p"]==0):
        return "YES"
    if(counter["p"]==1 and s[-1]=="p"):
        return "YES"
    elif(counter["s"]==1 and s[0]=="s"):
        return "YES"
    else:
        return "NO"    


t=1
t=cinint()
for _ in range(t):
    print(solve())
