from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    visited.add(start)

    traversal = []

    print("Starting BFS from:", start)
    print("Goal Node:", goal)
    print("----------------------")

    while queue:
        node = queue.popleft()
        traversal.append(node)

        # Show current node
        print("Visiting:", node)

        # Add unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

        # Show nodes currently in queue (the next nodes to visit)
        if queue:
            print("Nodes in queue:", list(queue))
        print()  # empty line for clarity

        # Check if goal is found
        if node == goal:
            print("Goal node", goal, "found!")
            print("\n BFS Traversal:", traversal)
            return


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

    bfs(graph, start_node, goal_node)