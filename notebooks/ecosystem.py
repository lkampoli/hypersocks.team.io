import json
import networkx as nx
import matplotlib.pyplot as plt

# Load the JSON data
with open('ecosystem.json', 'r') as file:
    data = json.load(file)

# Create a directed graph
G = nx.DiGraph()

# Recursive function to add nodes and edges
def add_nodes_edges(node, parent=None):
    G.add_node(node['name'])
    if parent:
        G.add_edge(parent, node['name'])
    for child in node.get('children', []):
        add_nodes_edges(child, node['name'])

# Add nodes and edges from the root
add_nodes_edges(data)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes

# Nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# Edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2)

# Labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

# Highlight different nodes
node_colors = []
for node in G.nodes():
    if node == "Competitors":
        node_colors.append('red')
    elif node == "Customers":
        node_colors.append('blue')
    else:
        node_colors.append('green')

nx.draw_networkx_nodes(G, pos, node_color=node_colors)

plt.title("Ecosystem Tree")
plt.show()

