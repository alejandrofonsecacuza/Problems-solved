def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n,a,b=cinline()
    if((abs(b-a)-1)%2==0):
        return "NO"
    else:
        return "YES" 
t=1
t=cinint()
for _ in range(t):
    print(solve())