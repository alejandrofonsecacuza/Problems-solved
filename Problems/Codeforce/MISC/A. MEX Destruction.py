
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    a=cinline()
    
    if(sum(a)==0):
        return 0
    for i in range(n):
        if(a[i]==0):
            a[i]=-1
        else:
            break
    for i in range(len(a)-1,0,-1):
        if(a[i]==0):
            a[i]=-1
        else:
            break
    for i in a:
        if(not i):
            return 2
    return 1


t=1
t=cinint()
for _ in range(t):
    print(solve())