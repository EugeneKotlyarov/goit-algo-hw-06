import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# G.add_edge('A', 'B')
# G.add_edge('A', 'C')
# G.add_edge('B', 'D')
# G.add_edge('C', 'D')
# G.add_edge('D', 'E')
# G.add_edge('E', 'F')
# G.add_edge('F', 'G')
# G.add_edge('G', 'H')
# G.add_edge('C', 'E')
# G.add_edge('G', 'C')

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

print(f"Маємо у графі {G.number_of_nodes()} вершин, {G.number_of_edges()} ребер")
print(f"Ступіні вершин:")
for node, degree in dict(G.degree()).items():
    print(f"├── {node}: {degree}")

pos = nx.spring_layout(G, seed=42)
nx.draw(
    G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
