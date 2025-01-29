def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
from collections import Counter
def solve():
    n,k=cinline()
    a=cinline()
    response=0
    counter=Counter(a)
    for i in counter:
        response+=min(counter[i],counter[(k-i)])
    return int(response/2)
t=1
t=cinint()
for _ in range(t):
    print(solve())