from collections import defaultdict
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def get_heights(root,tree,h,visited):
    visited[root]=True
    if len(tree[root])==1 or (not tree[root]):
        h[root]=(0,0)
        return h[root][0]
    height_aux=[-1]
    for n in tree[root]:
        if visited[n]:continue
        height_aux.append(get_heights(n,tree,h,visited))
    height_aux=sorted(height_aux,reverse=True)
    
    mx1=1+height_aux[0]
    mx2=1+height_aux[1]
    h[root]=(mx1,mx2)
    return h[root][0]

def distances(root,tree,response,visited,h,father):
    visited[root]=True
    response[root]=max(h[root],(response[father]+1))
    for n in tree[root]:
        if visited[n]:continue
        distances(n,tree,response,visited,h,root)            

def solve():
    n=cinint()
    tree=defaultdict(list)
    for _ in range(n-1):
        v1,v2=cinline()
        tree[v1].append(v2)
        tree[v2].append(v1)
    response=[-1]*(n+1)
    visited=[False]*(n+1)
    h=[-1]*(n+1)
    get_heights(1,tree,h,visited)
    print(f'{h=}')
    visited=[False]*(n+1)
    distances(1,tree,response,visited,h,0)
    return response
    

t=1
#t=cinint()
for _ in range(t):
    print(*solve()[1:])