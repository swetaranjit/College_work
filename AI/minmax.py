import math

def minimax_verbose(depth, node_index, is_max, scores, names):
    # Base Case: We've reached the bottom (the leaf scores)
    if depth == len(names) - 1:
        return scores[node_index]

    current_node = names[depth][node_index]
    player_type = "Maximizer" if is_max else "Minimizer"
    
    #print(f"--- Level {depth} ({player_type}) | Analyzing Node {current_node} ---")

    # Recurse to find values of children
    left_val = minimax_verbose(depth + 1, node_index * 2, not is_max, scores, names)
    right_val = minimax_verbose(depth + 1, node_index * 2 + 1, not is_max, scores, names)

    if is_max:
        result = max(left_val, right_val)
        print(f"Node {current_node} ({player_type}) picks max({left_val}, {right_val})")
    else:
        result = min(left_val, right_val)
        print(f"Node {current_node} ({player_type}) picks min({left_val}, {right_val})")

    print(f"Result: Node {current_node} is assigned value {result}\n")
    return result

# --- Setup the Tree ---
# Level 0: A
# Level 1: B, C
# Level 2: D, E, F, G
# Level 3: Leaf Scores
tree_names = [
    ["A"], 
    ["B", "C"], 
    ["D", "E", "F", "G"],
    ["Leaf", "Leaf", "Leaf", "Leaf", "Leaf", "Leaf", "Leaf", "Leaf"]
]

leaf_scores = [-1, 4, 2, 6, -3, -5, 0, 7]

# Start the algorithm
final_score = minimax_verbose(0, 0, True, leaf_scores, tree_names)
print(f"FINAL RESULT: The optimal value at Root Node A is {final_score}")