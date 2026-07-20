from collections import deque

def water_jug():
    visited = set()
    queue = deque([((0,0), [])])

    while queue:
        (a,b), path = queue.popleft()

        if (a,b) in visited:
            continue

        visited.add((a,b))
        path = path + [(a,b)]

        if a == 2:
            return path

        next_states = [
            (4,b),
            (a,3),
            (0,b),
            (a,0),
            (max(0,a-(3-b)), min(3,a+b)),
            (min(4,a+b), max(0,b-(4-a)))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

solution = water_jug()

print("Steps:")
for step in solution:
    print(step)
