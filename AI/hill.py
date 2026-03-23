import random

def objective_function(x):
    """
    The function we want to maximize. 
    Example: f(x) = -(x^2) + 4x + 10
    This is an inverted parabola with a peak at x = 2.
    """
    return -(x**2) + (4 * x) + 10

def hill_climbing(start_pos, step_size, max_iterations):
    current_pos = start_pos
    current_value = objective_function(current_pos)
    
    print(f"Starting at x = {current_pos:.2f}, value = {current_value:.2f}")
    
    for i in range(max_iterations):
        # Examine neighbors (slightly to the left and slightly to the right)
        next_pos_left = current_pos - step_size
        next_pos_right = current_pos + step_size
        
        val_left = objective_function(next_pos_left)
        val_right = objective_function(next_pos_right)
        
        # Determine if a neighbor is better than current position
        if val_left > current_value and val_left >= val_right:
            current_pos = next_pos_left
            current_value = val_left
            print(f"Step {i+1}: Moved Left to x = {current_pos:.2f}, value = {current_value:.2f}")
        elif val_right > current_value:
            current_pos = next_pos_right
            current_value = val_right
            print(f"Step {i+1}: Moved Right to x = {current_pos:.2f}, value = {current_value:.2f}")
        else:
            # If no neighbor is better, we have reached a peak (Local Optimum)
            print(f"\nReached a peak at step {i+1}!")
            break
            
    return current_pos, current_value

# --- Execution ---
initial_x = random.uniform(-10, 10)  # Pick a random starting point
increment = 0.1                      # How big each step is
limit = 100                          # Safety break to prevent infinite loops

best_x, best_val = hill_climbing(initial_x, increment, limit)

print(f"Final Solution: x = {best_x:.2f}, Maximum Value = {best_val:.2f}")