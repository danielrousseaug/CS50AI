"""Simple BFS search example for CS50 AI Week 0."""

from collections import deque

# Example graph of connections between people
GRAPH = {
    "Alice": {"Bob", "Claire"},
    "Bob": {"Dennis", "Elaine"},
    "Claire": {"Frank"},
    "Dennis": {"Gina"},
    "Elaine": {"Hank"},
    "Frank": {"Irene"},
    "Gina": set(),
    "Hank": {"Irene"},
    "Irene": set(),
}


def shortest_path(source: str, target: str):
    """Return the shortest path between source and target using BFS."""
    if source not in GRAPH or target not in GRAPH:
        raise ValueError("Person not in graph")

    frontier = deque([[source]])
    explored = set()

    while frontier:
        path = frontier.popleft()
        node = path[-1]
        if node == target:
            return path
        explored.add(node)
        for neighbor in GRAPH[node]:
            if neighbor not in explored:
                frontier.append(path + [neighbor])
    return None


def main():
    import sys
    if len(sys.argv) != 3:
        sys.exit("Usage: python degrees.py SOURCE TARGET")
    source, target = sys.argv[1], sys.argv[2]
    path = shortest_path(source, target)
    if path is None:
        print("No connection found.")
    else:
        print(" -> ".join(path))


if __name__ == "__main__":
    main()
