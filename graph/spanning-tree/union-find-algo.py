from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Find the subset of an element i 
    def findParent(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.findParent(parent, parent[i])

    def union(self, parent, x, y):
        setX = self.findParent(parent, x)
        setY = self.findParent(parent, y)
        parent[setX] = setY

    def isCyclic(self):
        parent = [-1] * self.vertices

        for i in self.graph:
            for j in self.graph[i]:
                x = self.findParent(parent, i)
                y = self.findParent(parent, j)

                if x == y:
                    return True
                else:
                    self.union(parent, x, y)

if __name__ == '__main__':
    g = Graph(3)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)

    if g.isCyclic():
        print('Graph contains a cycle')
    else:
        print('Graph does not contain a cycle.')

# Reference: https://www.youtube.com/watch?v=mHz-mx-8lJ8
# Reference: https://www.geeksforgeeks.org/union-find/