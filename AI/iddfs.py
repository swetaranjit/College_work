# Iterative Deepening Depth First Search (IDDFS)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'K': []
}

def dls(node, goal, limit, path):
    
    print(node, end=" ")   # traversal
    path.append(node)
    
    if node == goal:
        return True
    
    if limit <= 0:
        path.pop()
        return False
    
    for child in graph[node]:
        if dls(child, goal, limit - 1, path):
            return True
    
    path.pop()
    return False


def iddfs(start, goal, max_depth):
    
    for depth in range(max_depth + 1):
        print("\nDepth Level:", depth)
        path = []
        
        if dls(start, goal, depth, path):
            print("\nGoal found!")
            print("Path:", " -> ".join(path))
            return
    
    print("\n\nGoal not found within max depth")


start = 'A'
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

iddfs(start, goal, max_depth)