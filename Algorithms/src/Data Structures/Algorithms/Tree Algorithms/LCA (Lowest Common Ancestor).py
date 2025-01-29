def find_lca(root, p, q):
    if not root:
        return None
    if root.value == p or root.value == q:
        return root
    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right