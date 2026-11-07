graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def bfs(start, goal):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            visited.append(node)

            if node == goal:
                return path

            for child in graph[node]:
                new_path = path + [child]
                queue.append(new_path)

    return None


def dfs(start, goal):
    stack = [[start]]
    visited = []

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.append(node)

            if node == goal:
                return path

            for child in reversed(graph[node]):
                new_path = path + [child]
                stack.append(new_path)

    return None


print("BREADTH FIRST SEARCH")
print("Path:", " -> ".join(bfs('A', 'G')))

print()

print("DEPTH FIRST SEARCH")
print("Path:", " -> ".join(dfs('A', 'G')))