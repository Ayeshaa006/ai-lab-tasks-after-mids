#AI lab task 08:
#min max algorithm:
import math 
def minimax(current_depth, node_index, is_max_player, scores, total_depth):
    if current_depth == total_depth:
        return scores[node_index]
    if is_max_player:
        left_child = minimax(current_depth + 1, node_index * 2, False, scores, total_depth)
        right_child = minimax(current_depth + 1, node_index * 2 + 1, False, scores, total_depth)
        return max(left_child, right_child)
    else:
        left_child = minimax(current_depth + 1, node_index * 2, True, scores, total_depth)
        right_child = minimax(current_depth + 1, node_index * 2 + 1, True, scores, total_depth)
        return min(left_child, right_child)
leaf_scores = [3, 5, 2, 9]
depth_of_tree = int(math.log(len(leaf_scores), 2))
#result
result = minimax(0, 0, True, leaf_scores, depth_of_tree)
print(f"the optimal value found by minimax is: {result}")

