from collections import deque


vertices = ['A', 'B', 'C', 'D', 'E']



graph_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C']
}

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for neighbour in graph_list[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return visited



graph_matrix = [
   
    [0, 1, 1, 0, 0], 
    [1, 0, 0, 1, 1],  
    [1, 0, 0, 0, 1], 
    [0, 1, 0, 0, 0],  
    [0, 1, 1, 0, 0]   
]

def dfs(node, visited):
    visited[node] = True

    print(vertices[node], end=" ")

    for i in range(len(vertices)):
        if graph_matrix[node][i] == 1 and not visited[i]:
            dfs(i, visited)

print("BFS Traversal:")
print(*bfs('A'))

print("\nDFS Traversal:")

visited = [False] * len(vertices)


dfs(0, visited)