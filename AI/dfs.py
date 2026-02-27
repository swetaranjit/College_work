def dfs(graph, current, goal, visited=None, traversal=None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []

    print("Visiting:", current)
    visited.add(current)
    traversal.append(current)

    print("Visited Nodes:", visited)
    print()

    # Check if goal is found
    if current == goal:
        print("Goal node", goal, "found!")
        print("\nDFS Traversal:", traversal)
        return True

    # Visit neighbors
    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited, traversal):
                return True

    return False


# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    goal_node = 'F'

    print("Starting DFS from:", start_node)
    print("Goal Node:", goal_node)
    print("----------------------")

    dfs(graph, start_node, goal_node)