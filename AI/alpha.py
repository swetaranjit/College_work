import math

def alpha_beta_trace(depth, node_index, is_max, scores, names, alpha, beta):
    if depth == 3:
        return scores[node_index]

    current_node = names[depth][node_index]
    
    if is_max:
        # Evaluate Left Child
        left_val = alpha_beta_trace(depth + 1, node_index * 2, False, scores, names, alpha, beta)
        alpha = max(alpha, left_val)
        
        # Check if we should prune the Right Child
        if beta <= alpha:
            print(f"Node {current_node} (Maximizer) picks {left_val}")
            print(f"Result: Node {current_node} is assigned value {left_val}")
            print(f"PRUNED: Right child of {current_node} because Alpha({alpha}) >= Beta({beta})\n")
            return alpha
        
        # If not pruned, evaluate Right Child
        right_val = alpha_beta_trace(depth + 1, node_index * 2 + 1, False, scores, names, alpha, beta)
        res = max(left_val, right_val)
        print(f"Node {current_node} (Maximizer) picks max({left_val}, {right_val})")
        print(f"Result: Node {current_node} is assigned value {res}\n")
        return res

    else:
        # Evaluate Left Child
        left_val = alpha_beta_trace(depth + 1, node_index * 2, True, scores, names, alpha, beta)
        beta = min(beta, left_val)
        
        # Check if we should prune the Right Child
        if beta <= alpha:
            print(f"Node {current_node} (Minimizer) picks {left_val}")
            print(f"Result: Node {current_node} is assigned value {left_val}")
            print(f"PRUNED: Right child of {current_node} because Beta({beta}) <= Alpha({alpha})\n")
            return beta
        
        # If not pruned, evaluate Right Child
        right_val = alpha_beta_trace(depth + 1, node_index * 2 + 1, True, scores, names, alpha, beta)
        res = min(left_val, right_val)
        print(f"Node {current_node} (Minimizer) picks min({left_val}, {right_val})")
        print(f"Result: Node {current_node} is assigned value {res}\n")
        return res

# --- Data Setup ---
# Scores chosen to trigger pruning
leaf_scores = [3, 5, 2, 1, 12, 5, 23, 23]
node_names = [["A"], ["B", "C"], ["D", "E", "F", "G"]]

print("--- Alpha-Beta Pruning Step-by-Step ---\n")
alpha_beta_trace(0, 0, True, leaf_scores, node_names, -math.inf, math.inf)