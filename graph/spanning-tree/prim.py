import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printMst(self, parent):
        for i in range(1, self.vertices): 
            print(parent[i], "-", i, "\t", self.graph[i][ parent[i] ])

    def minKey(self, weightList, mstSet):
        minWeight = sys.maxsize

        for v in range(self.vertices):
            if weightList[v] < minWeight and mstSet[v] is False:
                minWeight = weightList[v]
                minIndex = v
        return minIndex

    def primMst(self):
        # weight values used to pick minimum weight edge in cut 
        weightList = [sys.maxsize] * self.vertices
        # Set to keep track of visited vertices
        mstSet = [False] * self.vertices
        # List to store constructed MST 
        parent = [None] * self.vertices

        # pick first/root vertex first
        weightList[0] = 0
        # root vertex has no parent
        parent[0] = -1

        for vertexIndex in range(self.vertices):
            # pick min weighted vertex/key
            u = self.minKey(weightList, mstSet)
            # set this vertex as traversed
            mstSet[u] = True

            for v in range(self.vertices):
                # graph[u][v] is non zero (means vertices are connected)
                # mstSet[v] is false (means it is not visited yet)
                # Update the key only if graph[u][v] is smaller than weightList[v] 
                if self.graph[u][v] > 0 and mstSet[v] is False and weightList[v] > self.graph[u][v]:
                    weightList[v] = self.graph[u][v]
                    parent[v] = u

        self.printMst(parent) 


if __name__ == '__main__':
    g = Graph(5)
    g.graph = [
        [0, 2, 0, 6, 0], 
        [2, 0, 3, 8, 5], 
        [0, 3, 0, 0, 7], 
        [6, 8, 0, 0, 9], 
        [0, 5, 7, 9, 0]
    ]
    g.primMst()