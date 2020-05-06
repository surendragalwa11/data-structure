# # Rank aporach of union-find algo to check for cycle
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

class Subset:
    def __init__(self, parent, rank = 0):
        self.parent = parent
        self.rank = rank

# find parent
def find(subSets, node):
    if subSets[node].parent != node:
        return find(subSets, subSets[node].parent)
    else:
        return subSets[node].parent

# union sets/nodes
def union(subSets, u, v):
    if subSets[u].rank > subSets[v].rank:
        subSets[v].parent = u
    elif subSets[u].rank < subSets[v].rank:
        subSets[u].parent = v
    else:
        subSets[v].parent = u
        subSets[u].rank += 1

def isCyclic(graph):
    subSets = [Subset(i) for i in range(g.vertices)]

    for u in graph.graph:
        rootU = find(subSets, u)

        for v in graph.graph[u]:
            rootV = find(subSets, v)

            if rootU == rootV:
                return True
            else:
                union(subSets, rootU, rootV)

if __name__ == '__main__':
    g = Graph(3)

    g.addEdge(0, 1)
    g.addEdge(1, 2)
    # g.addEdge(0, 2)

    if isCyclic(g):
        print('Graph contains a cycle.')
    else:
        print('Graph does not contain any cycle.')