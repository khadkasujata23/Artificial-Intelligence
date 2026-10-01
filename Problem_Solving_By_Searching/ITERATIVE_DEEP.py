def depth_limited_search(graph, current, goal, limit, depth=0, path=None):
    if path is None:
        path = []

    path.append(current)

    if current == goal:
        return path

    if depth == limit:
        path.pop()
        return None

    for neighbor in graph.get(current, []):
        if neighbor not in path:
            result = depth_limited_search(
                graph, neighbor, goal, limit, depth + 1, path
            )

            if result:
                return result

    path.pop()
    return None


# Graph
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": []
}


def iterative_deepening_search(graph, start, goal, max_depth=50):

    for depth in range(max_depth + 1):

        print("Searching with depth limit =", depth)

        result = depth_limited_search(
            graph, start, goal, depth
        )

        if result:
            return result

    return None


# Display graph
for key in graph:
    print(key, ":", graph[key])


# Input
start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()


# Check nodes
if start not in graph or goal not in graph:
    print("Invalid node")
else:

    # Perform Iterative Deepening Search
    path = iterative_deepening_search(graph, start, goal)

    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("Goal not found")