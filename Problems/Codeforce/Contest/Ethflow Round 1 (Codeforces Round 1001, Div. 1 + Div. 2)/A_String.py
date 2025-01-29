def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    s=list(map(int,list(input())))
    return sum(s)
t=1
t=cinint()
for _ in range(t):
    print(solve())