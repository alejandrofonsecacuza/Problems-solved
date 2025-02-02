def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

import bisect
def solve():
    n,q=cinline()
    a=cinline()
    
    query=cinline()
    for i in query:
        index=bisect.bisect_right(a,i)-1
        print(index)
        
        
t=1
#t=cinint()
for _ in range(t):
    (solve())