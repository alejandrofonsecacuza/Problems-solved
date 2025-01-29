def dfs_recursive(node, parent, graph):
    print(node, end=" ")  # Acción en el nodo actual
    for neighbor in graph[node]:
        if neighbor != parent:  # Evitamos regresar al padre
            dfs_recursive(neighbor, node, graph)

def dfs_iterative(start, graph):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Acción en el nodo actual
            visited.add(node)
            # Agregamos los vecinos al stack
            for neighbor in reversed(graph[node]):  # Invertir para mantener orden similar a DFS recursivo
                if neighbor not in visited:
                    stack.append(neighbor)


from collections import deque
def bfs(start, graph):
    queue = deque([start])
    visited = set()
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")  # Acción en el nodo actual
            visited.add(node)
            # Agregamos los vecinos a la cola
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


def dfs_preorder(node, graph, visited):
        if node not in visited:
            print(node, end=" ")  # Visita el nodo primero
            visited.add(node)
            for neighbor in graph[node]:  # Luego explora a sus vecinos
                dfs_preorder(neighbor, graph, visited)
def dfs_postorder(node, graph, visited):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:  # Explora a sus vecinos primero
                dfs_postorder(neighbor, graph, visited)
            print(node, end=" ")  # Visita el nodo después