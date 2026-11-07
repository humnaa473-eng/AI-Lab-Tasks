graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path + [node]

    if limit == 0:
        return "CUTOFF", None

    cutoff = False

    for child in graph[node]:
        if child not in path:
            result, found_path = dls(
                child, goal, limit - 1, path + [node]
            )

            if result == "FOUND":
                return result, found_path

            if result == "CUTOFF":
                cutoff = True

    if cutoff:
        return "CUTOFF", None

    return "FAILURE", None


print("DEPTH LIMITED SEARCH")

for limit in range(1, 5):
    result, path = dls('A', 'G', limit, [])

    print("Depth Limit:", limit)
    print("Result:", result)

    if path:
        print("Path:", " -> ".join(path))

    print()


print("ITERATIVE DEEPENING DFS")

for limit in range(5):
    result, path = dls('A', 'G', limit, [])

    print("Depth Limit:", limit)
    print("Result:", result)

    if path:
        print("Path:", " -> ".join(path))
        break

    print()