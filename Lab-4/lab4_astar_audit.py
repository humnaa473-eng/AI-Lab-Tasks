
# AI Lab 4
# Informed Search: Heuristics and A*
# Student Name: Humna Akbar
# Roll Number: 008


import heapq

# Graph
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
    "X": []
}

# Heuristic Values
heuristic = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0,
    "X": 0
}


# A* Algorithm
def astar(graph, h, start, goal):

    pq = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    processed = []
    expanded = []

    while pq:

        f, g, node, path = heapq.heappop(pq)

        if g != best_cost.get(node):
            continue

        processed.append(node)

        if node == goal:
            return g, path, processed, expanded

        expanded.append(node)

        for neighbor, cost in graph[node]:

            new_g = g + cost

            if new_g < best_cost.get(neighbor, float("inf")):

                best_cost[neighbor] = new_g
                new_f = new_g + h[neighbor]

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, None, processed, expanded


# Display Results
def show_result(title, result):

    cost, path, processed, expanded = result

    print("\n" + title)
    print("-----------------------------")

    if path:
        print("Path:", " -> ".join(path))
    else:
        print("Path: No path found")

    print("Total Cost:", cost)
    print("Processing Order:", processed)
    print("Expanded Nodes:", expanded)
    print("Expansion Count:", len(expanded))


print("AI LAB 4")
print("INFORMED SEARCH: A* AND UCS")


# Task 1: Original A*
result1 = astar(graph, heuristic, "S", "G")
show_result("TASK 1: ORIGINAL A*", result1)


# Task 2: Uniform Cost Search
zero_heuristic = {node: 0 for node in graph}

result2 = astar(graph, zero_heuristic, "S", "G")
show_result("TASK 2: UNIFORM COST SEARCH", result2)


# Task 3: Heuristic Overestimation
modified_heuristic = heuristic.copy()
modified_heuristic["C"] = 10

result3 = astar(graph, modified_heuristic, "S", "G")
show_result("TASK 3: MODIFIED HEURISTIC", result3)


# Edge Case: Unreachable Goal
result4 = astar(graph, heuristic, "S", "X")
show_result("EDGE CASE: UNREACHABLE GOAL", result4)
