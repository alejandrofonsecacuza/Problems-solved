from math import log
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    response=0
    e=int(log(n,5))
    for i in range(1,e+1):
        response+=(n//(5**i))
    return response
t=1
#=cinint()
for _ in range(t):
    print(solve())