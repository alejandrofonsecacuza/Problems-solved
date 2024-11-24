class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size  # Rango inicial para todos los nodos es 1
        self.count_sets=size

    def find(self, node):
        if self.parent[node] != node:
            # Compresión de caminos
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        count_sets-=1

        if root1 != root2:
            # Unión por rango
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1




		
Node=5
djset=UnionFind(Node)

djset.join(0,3)
djset.join(3,4)
djset.join(1,2)
djset.join(4,2)

for i in range(Node):
	print(djset.find(i))

















	



