# Type: Adjacency Matrix Implementation
class WeightedGraph:
    def __init__(self):
        self.vertices = []
        self.matrix = []

    def addVertex(self, id):
        if id not in self.vertices:
            self.vertices.append(id)
            verticesCount = len(self.vertices)
            self.matrix.append([0 for _ in range(verticesCount)])
            
            for i in range(verticesCount-1):
                self.matrix[i].append(0)

    def addEdge(self, vertex1, vertex2, weight = 0):
        if vertex1 not in self.vertices:
            self.vertices.append(vertex1)

        if vertex2 not in self.vertices:
            self.vertices.append(vertex2)

        verticesCount = len(self.vertices)
        vertexOneIndex = self.vertices.index(vertex1)
        vertexTwoIndex = self.vertices.index(vertex2)
        
        self.matrix[vertexOneIndex][vertexTwoIndex] = weight

                

if __name__ == '__main__':
    g = WeightedGraph()

    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    
    g.addEdge(1, 2, 1)
    g.addEdge(1, 3, 1)
    g.addEdge(2, 3, 3)
    g.addEdge(3, 4, 4)
    g.addEdge(4, 1, 5)

    print(g.matrix)
    # o/p: [[0, 1, 1, 0], [0, 0, 3, 0], [0, 0, 0, 4], [5, 0, 0, 0]]