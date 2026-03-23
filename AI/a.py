import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority queue for open list: (f_score, current_node, path_taken, g_score)
    open_list = [(heuristics[start], start, [start], 0)]
    closed_list = set()

    print(f"\n--- Starting A* Search: {start} -> {goal} ---")

    while open_list:
        # Sort is handled by heapq (pops lowest f_score)
        f, current, path, g = heapq.heappop(open_list)

        if current in closed_list:
            continue

        print(f"\nEvaluating Node: {current}")
        print(f"Closed List: {list(closed_list)}")
        
        # Goal Check
        if current == goal:
            print(f"Goal {goal} found!")
            return path, g

        closed_list.add(current)

        # Explore neighbors
        for neighbor, weight in graph.get(current, {}).items():
            if neighbor not in closed_list:
                g_neighbor = g + weight
                h_neighbor = heuristics.get(neighbor, 0)
                f_neighbor = g_neighbor + h_neighbor
                
                heapq.heappush(open_list, (f_neighbor, neighbor, path + [neighbor], g_neighbor))
        
        # Display the Open List in a readable format [(Node, f=g+h), ...]
        readable_open = [(item[1], f"f={item[0]} (g={item[3]}, h={item[0]-item[3]})") for item in open_list]
        print(f"Open List: {readable_open}")

    return None, float('inf')

# --- Data ---
graph = {
    'A': {'B': 2, 'C': 4, 'D': 3},
    'B': {'E': 5, 'F': 2},
    'C': {'G': 2, 'H': 6},
    'D': {'I': 4},
    'E': {},
    'F': {'J': 3},
    'G': {},
    'H': {'K': 2},
    'I': {'L': 1},
    'J': {},
    'K': {},
    'L': {}
}

heuristic = {
    'A': 10, 'B': 8, 'C': 7, 'D': 9,
    'E': 5, 'F': 4, 'G': 6, 'H': 3,
    'I': 2, 'J': 1, 'K': 0, 'L': 0
}

# --- User Interaction ---
print("Available Nodes:", ", ".join(graph.keys()))
user_goal = input("Enter the goal node: ").upper()

if user_goal not in graph:
    print("Invalid node! Please run the script again and pick a node from the list.")
else:
    result_path, total_cost = a_star_search(graph, heuristic, 'A', user_goal)
    
    if result_path:
        print(f"\nSUCCESS: Path to {user_goal} is {result_path}")
        print(f"Total Path Cost: {total_cost}")
    else:
        print(f"\nFAILURE: No path found to {user_goal}")