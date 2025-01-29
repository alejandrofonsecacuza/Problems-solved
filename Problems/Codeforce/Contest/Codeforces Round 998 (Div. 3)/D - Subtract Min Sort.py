def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    a=cinline()
    for i in range(n-1):
        minim=min(a[i],a[i+1])
        a[i]-=minim
        a[i+1]-=minim
        if(a[i]>a[i+1]):
            return "NO"
    return "YES"
t=1
t=cinint()
for _ in range(t):
    print(solve())