import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def uniform_cost_search(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)

            for neighbour, weight in graph[node]:
                heapq.heappush(queue,
                               (cost + weight,
                                neighbour,
                                path + [neighbour]))

cost, path = uniform_cost_search(graph, 'A', 'F')

print("Least Cost:", cost)
print("Path:", " -> ".join(path))
