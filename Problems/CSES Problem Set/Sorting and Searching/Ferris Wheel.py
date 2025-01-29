cinint = lambda: int(input())
cinline = lambda: list(map(int,input().split()))
from collections import deque
def solve():
    n,x=cinline()
    p=cinline()
    p=deque(sorted(p))
    response=0
    while p:
        if(len(p)==1):
            response+=1
            p.pop()
            continue
        w=p[0]+p[-1]
        if w<=x:
            response+=1
            p.popleft()
            p.pop()
        else:
            p.pop()
            response+=1
    return response
        
    
t=1
#t=cinint()
for _ in range(t):
    print(solve())