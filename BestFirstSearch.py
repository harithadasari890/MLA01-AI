import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

def best_first_search(start, goal):
    visited = set()
    queue = [(heuristic[start], start)]

    while queue:
        h, node = heapq.heappop(queue)

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if node == goal:
                return

            for neighbour in graph[node]:
                heapq.heappush(queue,
                               (heuristic[neighbour], neighbour))

print("Best First Search Traversal:")
best_first_search('A', 'F')
