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
class Binary_Search_Tree():    
    """
    A class representing a BST.
    Attributes:
    root : Node
        The root node of the BST
    """
    def __init__(self):
        """
        Initializes an empty BST.
        """
        self.root = None
    def insert(self,value):
        self.root=self._insert(self.root,value)
        
    def _insert(self,root,value):
        if(root is None):
            return Node(value)
        elif value>=root.value:
            root.right=self._insert(root.right,value)
        else:
            root.left=self._insert(root.left,value)
        return root
    
    def search(self,value):
        return self._search(self.root,value)
    def _search(self,root,value):
        if root is None:
            return False    
        if value>root.value:
            return self._search(root.right,value)
        elif value<root.value:
            return self._search(root.left,value)
        else:
            return True
        
    def in_order(self):
        path=[]
        self._in_order(self.root,path)
        return path
    def _in_order(self,node,path):
        if node:
            self._in_order(node.left,path)
            path.append(node.value)
            self._in_order(node.right,path)
            
        pass
if __name__=="__main__":
    bst=Binary_Search_Tree()
    nodes=[5,7,3,10,6,4,2,1]
    for n in nodes:
        bst.insert(n)
    print(bst.in_order())
    nodes=[8,6,4,9,1]
    
    for n in nodes:
        print(f'{n=}')
        print(bst.search(n))