def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
from collections import defaultdict
def solve():
    #traslate to c++ to accepted
    n,x=cinline()
    a=cinline()
    memo=defaultdict(lambda:-1)
    for index,value in enumerate(a):
        if memo[x-value]!=-1:
            return [index+1,memo[x-value]+1]
        else:
            memo[value]=index
    return ["IMPOSSIBLE" ]   
        
t=1
#t=cinint()
for _ in range(t):
    print(*solve())