import heapq

graph = {
    'A': [('B', 1), ('C', 6)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 4), ('G', 6)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}


def ucs(start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()
    processing_order = []

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        processing_order.append(node)

        if node == goal:
            return path, cost, processing_order

        for child, weight in graph[node]:
            if child not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + weight, child, path + [child])
                )

    return None, None, processing_order


def bfs(start, goal):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path

        for child, weight in graph[node]:
            if child not in visited:
                queue.append(path + [child])

    return None


print("UNIFORM COST SEARCH")

path, cost, order = ucs('A', 'G')

print("Processing Order:", order)
print("UCS Path:", " -> ".join(path))
print("Total Cost:", cost)

print()

print("BREADTH FIRST SEARCH")

bfs_path = bfs('A', 'G')

bfs_cost = 0

for i in range(len(bfs_path) - 1):
    for child, weight in graph[bfs_path[i]]:
        if child == bfs_path[i + 1]:
            bfs_cost += weight

print("BFS Path:", " -> ".join(bfs_path))
print("Total Cost:", bfs_cost)