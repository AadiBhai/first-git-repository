graph = {
    'A': ['A', 'C'],
    'B': ['B', 'E'],
    'C': ['D'],
    'D': ['F'],
    'E': [],
    'F': ['D']
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')