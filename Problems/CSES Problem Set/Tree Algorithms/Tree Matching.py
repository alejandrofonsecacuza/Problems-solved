from collections import defaultdict
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
import sys

# Aumentar el límite de recursión a 5000
sys.setrecursionlimit(50000)
def matching(root,tree,visited):
    band=True
    visited[root]=True
    
    if not tree[root]:
        #print(f'{root=}')
        #print("count=0")
        #print("band= False")
        return 0,False
    count=0
    for child in tree[root]:
        if visited[child]:continue
        c,b=matching(child,tree,visited)
        count+=c
        band = band and b
        
    if not band:    
        count += 1  
        band=True
    else:
        band=False
    #print(f'{root=}')
        
    #print(f'{count=}')
    #print(f'{band=}')
    return count,band
def solve():
    tree=defaultdict(list)
    n=cinint()
    for _ in range(n-1):
        v1,v2=cinline()
        tree[v1].append(v2)
        tree[v2].append(v1)
    return matching(1,tree,visited=([False]*(n+1)))[0]

            
t=1
#t=cinint()
for _ in range(t):
    print(solve())