def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

def f(x):
    return (1/2)*(x**4)-(9/2)*(x**2)+(12*x)-8
def solve():
    n=cinint()
    for i in range(1,n+1):
        print(int(f(i)))
t=1
#t=cinint()
for _ in range(t):
    (solve())