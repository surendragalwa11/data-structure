from collections import defaultdict

# Type: Adjacency list Implementation
class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent = []

    
    def addNeighbour(self, neighbour, weight = 0):
        self.adjacent.append([neighbour, weight])

    def getNeighbour(self):
        return self.adjacent

    def getId(self):
        return self.id

class WeightedGraph:
    def __init__(self):
        self.vertices = defaultdict(list)
        self.verticesCount = 0

    def addVertex(self, id):
        vertex = Vertex(id)
        self.vertices[id] = vertex
        return vertex

    def getVertex(self, id):
        if id in self.vertices:
            return self.vertices[id]
        else:
            return None

    def addEdge(self, vertex1, vertex2, weight = 0):
        if vertex1 not in self.vertices:
            self.addVertex(vertex1)
        
        if vertex2 not in self.vertices:
            self.addVertex(vertex2)

        self.vertices[vertex1].addNeighbour(vertex2, weight)
        self.vertices[vertex2].addNeighbour(vertex1, weight)

    def getVertices(self):
        return self.vertices.keys()

    def printGraph(self):
        for vertex in self.vertices.keys():
            print(vertex, self.vertices[vertex].getNeighbour())

if __name__ == '__main__':

    g = WeightedGraph()

    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')

    g.addEdge('a', 'b', 7)  
    g.addEdge('a', 'c', 9)
    g.addEdge('a', 'f', 14)
    g.addEdge('b', 'c', 10)
    g.addEdge('b', 'd', 15)
    g.addEdge('c', 'd', 11)
    g.addEdge('c', 'f', 2)
    g.addEdge('d', 'e', 6)
    g.addEdge('e', 'f', 9)

    print(g.vertices)
    g.printGraph()
    # o/p:
    #  a [['b', 7], ['c', 9], ['f', 14]]
    # b [['a', 7], ['c', 10], ['d', 15]]
    # c [['a', 9], ['b', 10], ['d', 11], ['f', 2]]
    # d [['b', 15], ['c', 11], ['e', 6]]
    # e [['d', 6], ['f', 9]]
    # f [['a', 14], ['c', 2], ['e', 9]]
