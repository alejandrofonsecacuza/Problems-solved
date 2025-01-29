def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve1():
    n=cinint()
    a=[0]+cinline()
    results=[]
    ans=sum(a)

    b = [0] * (n + 1)
    for i in range(1, n):
        ans = max(ans, abs(a[n - i + 1] - a[1]))
        for j in range(1, n - i + 1):
            b[j] = a[j + 1] - a[j]

        for j in range(1, n - i + 1):
            a[j] = b[j]

    return ans
  
t=1
t=cinint()
for _ in range(t):
    print(solve1())

