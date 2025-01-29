def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

import sys

# Aumentar el límite de recursión a 5000
sys.setrecursionlimit(5000)
def get_subordinates(root,tree,arr):
    #print(f'{root=}')
    if not tree[root]:
        return 0
    count_n=0
    for n in tree[root]:
        count_n+=get_subordinates(n,tree,arr)
    count_n+=len(tree[root])
    arr[root]=count_n
    return count_n

def solve():
    n=cinint()
    a=cinline()
    tree={node:[] for node in range(1,n+1) }
    for index,value in enumerate(a):
        tree[value].append(index+2)
    #print(f'{tree=}')
    arr=[0]*(n+1)
    get_subordinates(1,tree,arr)
    #print(f'{get_subordinates(1,tree,arr)=}')
    return arr[1:]
t=1
#t=cinint()
for _ in range(t):
    print(*solve())