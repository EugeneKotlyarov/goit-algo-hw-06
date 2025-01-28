import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from(
    [
        ("A", "C"),
        ("B", "C"),
        ("A", "E"),
        ("B", "D"),
        ("D", "E"),
        ("F", "G"),
        ("G", "H"),
        ("G", "C"),
        ("B", "E"),
        ("B", "F"),
    ]
)


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for neighbor in set(graph.neighbors(node)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            stack.append((neighbor, path + [neighbor]))
    return None


def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        for neighbor in set(graph.neighbors(node)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            queue.append((neighbor, path + [neighbor]))
    return None


def main():

    start, goal = "E", "H"
    dfs_result = dfs_path(G, start, goal)
    bfs_result = bfs_path(G, start, goal)
    print("DFS:", dfs_result)
    print("BFS:", bfs_result)

    start, goal = "D", "H"
    dfs_result = dfs_path(G, start, goal)
    bfs_result = bfs_path(G, start, goal)
    print("DFS:", dfs_result)
    print("BFS:", bfs_result)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=15,
        width=2,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()


if __name__ == "__main__":
    main()
