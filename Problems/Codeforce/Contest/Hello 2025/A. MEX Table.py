def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n,m=cinline()
    return max(n,m)+1
t=1
t=cinint()
for _ in range(t):
    print(solve())