# This alogo uses union-find approach
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)

        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


    def kruskalMst(self):
        #This will store the resultant MST 
        result = []
        #This will store the parents for each node
        parent = []
        #This will store the parents for each node
        rank = []
         # An index variable, used for sorted edges 
        i = 0
        # An index variable, used for result[] or number of edges processed
        e = 0

        print(self.graph)
        # Sort all the edges in non-decreasing order of their weight. 
        self.graph = sorted(self.graph, key = lambda item: item[2])
        print(self.graph)

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while e < (self.vertices - 1):
            u, v, w = self.graph[i]
            i = i + 1

            rootX = self.find(parent, u)
            rootY = self.find(parent, v)

            if rootX != rootY:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, rootX, rootY)

        print("Following are the edges in the constructed MST")
        for u, v, w in result:
            print ("%d -- %d == %d" % (u, v, w))

    
if __name__ == '__main__':
    g = Graph(4) 
    g.addEdge(0, 1, 10) 
    g.addEdge(0, 2, 6) 
    g.addEdge(0, 3, 5) 
    g.addEdge(1, 3, 15) 
    g.addEdge(2, 3, 4)

    g.kruskalMst() 
