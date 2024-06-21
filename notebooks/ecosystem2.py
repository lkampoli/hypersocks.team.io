import json
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import matplotlib.pyplot as plt
from PIL import Image

# Load the JSON data
with open('ecosystem.json', 'r') as file:
    data = json.load(file)

# Recursive function to create the tree
def create_tree(node, parent=None):
    current_node = Node(node['name'], parent=parent)
    for child in node.get('children', []):
        create_tree(child, current_node)
    return current_node

# Create the tree from the root
root = create_tree(data)

# Print the tree structure
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")

# Export the tree to a dot file and visualize
DotExporter(root).to_dotfile("tree.dot")

# Convert the dot file to an image and display it
import subprocess
subprocess.run(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png'], check=True)

# Display the image
img = Image.open('tree.png')
plt.figure(figsize=(20, 20))
plt.imshow(img)
plt.axis('off')
plt.show()

