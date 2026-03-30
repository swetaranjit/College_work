import itertools

def solve_multi_city_tsp():
    # 1. Pre-defined Data: 10 Cities
    # Index: 0:London, 1:Paris, 2:Berlin, 3:Rome, 4:Madrid, 5:Amsterdam, 6:Vienna, 7:Prague, 8:Brussels, 9:Zurich
    locations = [
        "London", "Paris", "Berlin", "Rome", "Madrid", 
        "Amsterdam", "Vienna", "Prague", "Brussels", "Zurich"
    ]
    
    # Distance Matrix (approximate relative distances)
    # Rows and Columns follow the order of the 'locations' list above
    dist_matrix = [
        [0, 344, 932, 1435, 1264, 358, 1235, 1032, 320, 778],   # London
        [344, 0, 878, 1105, 1052, 430, 1034, 885, 264, 489],    # Paris
        [932, 878, 0, 1184, 1870, 595, 524, 280, 651, 672],     # Berlin
        [1435, 1105, 1184, 0, 1362, 1297, 765, 922, 1173, 687], # Rome
        [1264, 1052, 1870, 1362, 0, 1482, 1809, 1775, 1315, 1148], # Madrid
        [358, 430, 595, 1297, 1482, 0, 937, 710, 173, 603],     # Amsterdam
        [1235, 1034, 524, 765, 1809, 937, 0, 253, 915, 591],    # Vienna
        [1032, 885, 280, 922, 1775, 710, 253, 0, 718, 526],     # Prague
        [320, 264, 651, 1173, 1315, 173, 915, 718, 0, 492],     # Brussels
        [778, 489, 672, 687, 1148, 603, 591, 526, 492, 0]       # Zurich
    ]

    print("--- 🌍 Global City Route Optimizer ---")
    print("Available Cities:")
    # Print cities in 2 columns for readability
    for i in range(0, len(locations), 2):
        print(f"• {locations[i]:<12} • {locations[i+1]:<12}")

    # 2. User Input
    print("\nSelect your starting city and your destinations.")
    start_city_name = input("Starting City: ").strip()
    
    if start_city_name not in locations:
        print(f"Sorry, '{start_city_name}' is not in our database.")
        return

    dest_input = input("Enter other destinations (comma-separated): ")
    dest_names = [name.strip() for name in dest_input.split(",")]

    # Map names to indices
    start_idx = locations.index(start_city_name)
    visit_indices = [start_idx]
    
    for name in dest_names:
        if name in locations and name != start_city_name:
            visit_indices.append(locations.index(name))
        elif name == start_city_name:
            continue
        else:
            print(f"⚠️ Skipping '{name}' (Not found)")

    if len(visit_indices) < 2:
        print("You need at least a starting city and one destination!")
        return

    # 3. Solve for selected cities
    # We find the best permutation of the 'other' cities
    other_cities = visit_indices[1:]
    best_path = None
    min_cost = float('inf')

    for p in itertools.permutations(other_cities):
        path = [start_idx] + list(p) + [start_idx]
        cost = 0
        for i in range(len(path) - 1):
            cost += dist_matrix[path[i]][path[i+1]]
        
        if cost < min_cost:
            min_cost = cost
            best_path = path

    # 4. Final Result
    print("\n" + "═"*40)
    print(f"🚩 OPTIMAL ROUTE FROM {start_city_name.upper()}")
    print("═"*40)
    
    for i in range(len(best_path) - 1):
        u, v = best_path[i], best_path[i+1]
        print(f"Step {i+1}: {locations[u]:<10} ➔  {locations[v]:<10} (Dist: {dist_matrix[u][v]})")
    
    print("-" * 40)
    print(f"Total Journey Distance: {min_cost} km")
    print("═"*40)

if __name__ == "__main__":
    solve_multi_city_tsp()