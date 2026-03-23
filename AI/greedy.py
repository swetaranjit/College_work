import heapq

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': [],
    'F': ['J'],
    'G': [],
    'H': ['K'],
    'I': ['L'],
    'J': [],
    'K': [],
    'L': []
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 10, 'B': 8, 'C': 7, 'D': 9,
    'E': 5, 'F': 4, 'G': 6, 'H': 3,
    'I': 2, 'J': 1, 'K': 0, 'L': 0
}


def greedy_best_first(start, goal):
    
    visited = set()
    pq = []
    
    heapq.heappush(pq, (heuristic[start], start))
    
    path = []
    
    print("Traversal Order:")
    
    while pq:
        h, node = heapq.heappop(pq)
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            path.append(node)
            
            if node == goal:
                print("\nGoal node found")
                print("Path:", " -> ".join(path))
                return
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristic[neighbor], neighbor))
    
    print("\nGoal not found")


start = 'A'
goal = input("Enter goal node: ")

greedy_best_first(start, goal)