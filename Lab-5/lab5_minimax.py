

# AI Lab 5
# Minimax and Alpha-Beta Pruning
# Student Name: Humna Akbar
# Roll Number: 008


# Minimax Algorithm
def minimax(depth, node, is_max, scores, target_depth):

    if depth == target_depth:
        return scores[node], 1

    if is_max:
        left, count1 = minimax(
            depth + 1, node * 2, False, scores, target_depth
        )
        right, count2 = minimax(
            depth + 1, node * 2 + 1, False, scores, target_depth
        )

        return max(left, right), count1 + count2

    else:
        left, count1 = minimax(
            depth + 1, node * 2, True, scores, target_depth
        )
        right, count2 = minimax(
            depth + 1, node * 2 + 1, True, scores, target_depth
        )

        return min(left, right), count1 + count2


# Alpha-Beta Pruning
def alpha_beta(depth, node, is_max, scores,
               target_depth, alpha, beta):

    if depth == target_depth:
        return scores[node], 1

    count = 0

    if is_max:
        best = float("-inf")

        for child in [node * 2, node * 2 + 1]:

            value, visited = alpha_beta(
                depth + 1, child, False, scores,
                target_depth, alpha, beta
            )

            count += visited
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best, count

    else:
        best = float("inf")

        for child in [node * 2, node * 2 + 1]:

            value, visited = alpha_beta(
                depth + 1, child, True, scores,
                target_depth, alpha, beta
            )

            count += visited
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best, count


# Task 1: Minimax
scores1 = [3, 5, 2, 9, 0, 7, 0, 0]

value1, count1 = minimax(
    0, 0, True, scores1, 3
)

print("TASK 1: MINIMAX")
print("Best Value:", value1)
print("Leaf Nodes Visited:", count1)


# Task 2: Alpha-Beta Pruning
scores2 = [3, 5, 2, 9, 3, 5, 2, 9]

value2, count2 = alpha_beta(
    0, 0, True, scores2, 3,
    float("-inf"), float("inf")
)

print("\nTASK 2: ALPHA-BETA PRUNING")
print("Best Value:", value2)
print("Leaf Nodes Visited:", count2)


# Task 3: Reordered Values
scores3 = [9, 2, 5, 3, 9, 2, 5, 3]

value3, count3 = alpha_beta(
    0, 0, True, scores3, 3,
    float("-inf"), float("inf")
)

print("\nTASK 3: REORDERED VALUES")
print("Best Value:", value3)
print("Leaf Nodes Visited:", count3)


# Edge Case: Single Leaf
scores4 = [7]

value4, count4 = minimax(
    0, 0, True, scores4, 0
)

print("\nEDGE CASE: SINGLE LEAF")
print("Best Value:", value4)
print("Leaf Nodes Visited:", count4)