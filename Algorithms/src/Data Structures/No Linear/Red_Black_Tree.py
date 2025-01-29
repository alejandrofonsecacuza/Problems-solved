# Definición de la clase Node (Nodo)
class Node:
    def __init__(self, key, color="RED"):
        self.left = None    # Hijo izquierdo
        self.right = None   # Hijo derecho
        self.parent = None  # Padre
        self.val = key      # Valor del nodo
        self.color = color  # Color del nodo (RED o BLACK)

# Función para realizar una rotación simple a la izquierda (RR)
def rotate_left(tree, x):
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:
        tree = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    return tree

# Función para realizar una rotación simple a la derecha (LL)
def rotate_right(tree, y):
    x = y.left
    y.left = x.right
    if x.right is not None:
        x.right.parent = y
    x.parent = y.parent
    if y.parent is None:
        tree = x
    elif y == y.parent.right:
        y.parent.right = x
    else:
        y.parent.left = x
    x.right = y
    y.parent = x
    return tree

# Función para insertar un nuevo nodo en el árbol rojo-negro
def insert(tree, key):
    # Paso 1: Inserción estándar en un BST
    new_node = Node(key)
    if tree is None:
        new_node.color = "BLACK"  # La raíz siempre es negra
        return new_node

    parent = None
    current = tree
    while current is not None:
        parent = current
        if key < current.val:
            current = current.left
        else:
            current = current.right

    new_node.parent = parent
    if key < parent.val:
        parent.left = new_node
    else:
        parent.right = new_node

    # Paso 2: Ajustar el árbol para mantener las propiedades del árbol rojo-negro
    tree = fix_insert(tree, new_node)
    return tree

# Función para ajustar el árbol después de una inserción
def fix_insert(tree, node):
    while node.parent is not None and node.parent.color == "RED":
        if node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
            if uncle is not None and uncle.color == "RED":
                # Caso 1: El tío es rojo
                node.parent.color = "BLACK"
                uncle.color = "BLACK"
                node.parent.parent.color = "RED"
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    # Caso 2: El tío es negro y el nodo es un hijo derecho
                    node = node.parent
                    tree = rotate_left(tree, node)
                # Caso 3: El tío es negro y el nodo es un hijo izquierdo
                node.parent.color = "BLACK"
                node.parent.parent.color = "RED"
                tree = rotate_right(tree, node.parent.parent)
        else:
            uncle = node.parent.parent.left
            if uncle is not None and uncle.color == "RED":
                # Caso 1: El tío es rojo
                node.parent.color = "BLACK"
                uncle.color = "BLACK"
                node.parent.parent.color = "RED"
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    # Caso 2: El tío es negro y el nodo es un hijo izquierdo
                    node = node.parent
                    tree = rotate_right(tree, node)
                # Caso 3: El tío es negro y el nodo es un hijo derecho
                node.parent.color = "BLACK"
                node.parent.parent.color = "RED"
                tree = rotate_left(tree, node.parent.parent)

    tree.color = "BLACK"  # La raíz siempre es negra
    return tree

# Recorrido Inorden (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Función principal para probar el árbol rojo-negro
if __name__ == "__main__":
    # Crear un árbol rojo-negro
    tree = None
    keys = [10, 20, 30, 15, 25, 5]

    for key in keys:
        tree = insert(tree, key)

    # Recorrido Inorden (debe devolver valores en orden ascendente)
    print("Recorrido Inorden:")
    inorder(tree)  # Salida: 5 10 15 20 25 30