import sys

sys.setrecursionlimit(500000)
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def diameter(root,tree,memo,visited):
    #print(f'{root=}')
    visited[root]=True
    if not tree[root]:
        return 1
    heights=[]
    for n in tree[root]:
        if visited[n]:continue
        #print(f'{root=}-{n=}')
        h=diameter(n,tree,memo,visited)
        heights.append(h)
    heights=sorted(heights,reverse=True)
    try:
        max_h1=heights[0]
    except:
        max_h1=0
    try:
        max_h2=heights[1]
    except:
        max_h2=0
    #print(f'{root=}:{max_h1=},{max_h2=}')
    memo[root]=max_h1+max_h2
    #print(f'{memo=}')
    return max_h1+1
    
from collections import defaultdict
def solve():
    n=cinint()
    if(n==1):return 0
    tree=defaultdict(list)
    for _ in range(n-1):
        v1,v2=cinline()
        tree[v1].append(v2)
        tree[v2].append(v1)
    #print(tree)
    memo=[-1]*(n+1)
    visited=[False]*(n+1)
    diameter(1,tree,memo,visited) 
    return sorted(memo,reverse=True)[0]  
t=1
#t=cinint()
for _ in range(t):
    print(solve())