from collections import deque

class Node():
    """
    A class representing a node in a binary tree.
    
    Attributes:
    value : any
        The value stored in the node.
    left : Node
        The left child node.
    right : Node
        The right child node.
    """
    def __init__(self, value=None):
        """
        Initializes a new node with the given value.
        
        Parameters:
        value : any, optional
            The value to be stored in the node (default is None).
        """
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree():
    """
    A class representing a binary tree.
    
    Attributes:
    root : Node
        The root node of the binary tree.
    """
    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a new node with the given value into the binary tree.
        
        Parameters:
        value : any
            The value to be inserted into the binary tree.
        """
        new_node = Node(value=value)
        if not self.root:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.left is None:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            if node.right is None:
                node.right = new_node
            else:
                queue.append(node.right)

    def in_order(self):
        """
        Performs an in-order traversal of the binary tree.
        
        Returns:
        list
            A list of values representing the in-order traversal of the binary tree.
        """
        path = []
        self._in_order(node=self.root, path=path)
        return path

    def _in_order(self, node, path):
        """
        A helper method to perform in-order traversal.
        
        Parameters:
        node : Node
            The current node in the traversal.
        path : list
            The list to store the traversal path.
        """
        if node is not None:
            self._in_order(node.left, path)
            path.append(node.value)
            self._in_order(node.right, path)
            
    def pre_order(self):
        """
        Performs an pre-order traversal of the binary tree.
        
        Returns:
        list
            A list of values representing the pre-order traversal of the binary tree.
        """
        path = []
        self._pre_order(node=self.root, path=path)
        return path

    def _pre_order(self, node, path):
        """
        A helper method to perform pre-order traversal.
        
        Parameters:
        node : Node
            The current node in the traversal.
        path : list
            The list to store the traversal path.
        """
        if node is not None:
            path.append(node.value)
            self._pre_order(node.left, path)
            self._pre_order(node.right, path)
            
    def post_order(self):
        """
        Performs an post-order traversal of the binary tree.
        
        Returns:
        list
            A list of values representing the post-order traversal of the binary tree.
        """
        path = []
        self._post_order(node=self.root, path=path)
        return path

    def _post_order(self, node, path):
        """
        A helper method to perform post-order traversal.
        
        Parameters:
        node : Node
            The current node in the traversal.
        path : list
            The list to store the traversal path.
        """
        if node is not None:
            self._post_order(node.left, path)
            self._post_order(node.right, path)
            path.append(node.value)
            