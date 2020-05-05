from collections import defaultdict

# Un weighted graph implementation
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.G = defaultdict(list)


    def addEdge(self, u, v):
        self.G[u].append(v)

if __name__ == '__main__':
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 0)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 4)
    g.addEdge(6, 7)
    print('Graph', g.G)
    # o/p: {0: [1], 1: [2], 2: [3, 4], 3: [0], 4: [5], 5: [6], 6: [4, 7]}