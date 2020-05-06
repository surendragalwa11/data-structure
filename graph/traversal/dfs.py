# Method: 1
# def dfsUtil(graph, root, visited):
#     visited.append(root)
#     neighbours = graph[root]
#     for neighbour in neighbours:
#         if neighbour not in visited:
#             dfsUtil(graph, neighbour, visited)
#     return visited

# def dfs(graph, root):
#     visited = []
#     visited = dfsUtil(graph, root, visited)
#     return visited

# Method 2
def dfs(graph, root, visited = []):
    if root not in visited:
        visited.append(root)
        for vertex in graph[root]:
            dfs(graph, vertex, visited)
    return visited



if __name__ == '__main__':
    # graph = {1: [2, 4, 5], 2: [3, 6, 7], 3: [], 4: [], 5: [], 6: [], 7: []}
    # visited = dfs(graph, 1)
    # print(visited)
    # o/p: [1, 2, 3, 6, 7, 4, 5]

    graph = {
        'A' : ['B','S'],
        'B' : ['A'],
        'C' : ['D','E','F','S'],
        'D' : ['C'],
        'E' : ['C','H'],
        'F' : ['C','G'],
        'G' : ['F','S'],
        'H' : ['E','G'],
        'S' : ['A','C','G']
    }
    visited = dfs(graph, 'A')
    print(visited)
    #o/p: ['A', 'B', 'S', 'C', 'D', 'E', 'H', 'G', 'F']