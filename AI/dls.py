# Depth Limited Search with traversal and path

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['I', 'J'],
    'C': ['E', 'F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': [],
    'I': ['H'],
    'J': [],
    'H': []
}

def depth_limited_search(node, goal, limit, path):
    
    print(node, end=" ")   # Traversal
    
    path.append(node)      # Add node to path
    
    if node == goal:
        return True
    
    if limit <= 0:
        path.pop()
        return False
    
    for child in graph[node]:
        if depth_limited_search(child, goal, limit - 1, path):
            return True
    
    path.pop()   # Remove node if not in solution path
    return False


start = 'S'
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

path = []

print("Traversal Order:")

if depth_limited_search(start, goal, limit, path):
    print("\nGoal node found within depth limit")
    print("Path to goal:", " -> ".join(path))
else:
    print("\nGoal node not found within depth limit")