def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    a=cinline()
    b=cinline()
    set_a=set(a)
    set_b=set(b)
    if(len(set_a)+len(set_b)>3):
        return "YES"
    else:
        return "NO"
t=1
t=cinint()
for _ in range(t):
    print(solve())