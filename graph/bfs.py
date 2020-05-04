import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root]) # when set has numbers
    # visited, queue = [], collections.deque([root]) # when set has string/char
    while queue:
        vertex = queue.popleft()
        print(vertex)
        visited.add(vertex)

        # for neighbour in graph[vertex]:
        #     if neighbour not in visited:
        #         queue.append(neighbour)
        queue.extend(neighbour for neighbour in graph[vertex] if neighbour not in visited)
    print(visited)

if __name__ == '__main__':
    # graph = {0: [1, 2], 1: [2], 2: []} 
    graph = {1: [2, 4, 5], 2: [3, 6, 7], 3: [], 4: [], 5: [], 6: [], 7: []}
    # graph = {'A': ['B', 'C', 'E'],
    #      'B': ['A','D', 'E'],
    #      'C': ['A', 'F', 'G'],
    #      'D': ['B'],
    #      'E': ['A', 'B','D'],
    #      'F': ['C'],
    #      'G': ['C']}
# ['A', 'B', 'C', 'E', 'D', 'F', 'G']

    bfs(graph, 1)