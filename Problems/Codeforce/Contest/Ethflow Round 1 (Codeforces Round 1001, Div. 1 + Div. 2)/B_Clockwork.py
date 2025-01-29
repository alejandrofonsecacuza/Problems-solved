def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    la=cinline()
    bool_var = True

    for i in range(n):
        l = i
        r = n - i - 1
        requirement = 2 * max(l, r) + 1

        if la[i] < requirement:
            return "NO"
        i += 1

    return "YES"
t=1
t=cinint()
for _ in range(t):
    print(solve())
    
    


