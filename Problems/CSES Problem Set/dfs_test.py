tree={1:[2,3,4],
      2:[5,6],
      3:[],
      4:[7],
      5:[],
      6:[],
      7:[],}

def dfs_recursivo_nario(nodo,tree):
    # Visitar el nodo (aquí simplemente imprimimos su valor)
    print(nodo,end=" ")
    # Recorrer todos los hijos
    for n in tree[nodo]:
        dfs_recursivo_nario(n,tree)
        
(dfs_recursivo_nario(1,tree))
from collections import deque
def dfs_iter(root,tree):
    stack=deque([root])
    while stack:
        node=stack.pop()
        print(node,end=" ")
        for n in reversed(tree[node]):
            stack.append(n)
        
print()
print("dfs_iterativo")
(dfs_iter(1,tree))