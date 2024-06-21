#import json
#from anytree import Node, RenderTree
#from anytree.exporter import DotExporter, LatexExporter
#
## Load the JSON data
#with open('ecosystem.json', 'r') as file:
#    data = json.load(file)
#
## Recursive function to create the tree
#def create_tree(node, parent=None):
#    current_node = Node(node['name'], parent=parent)
#    for child in node.get('children', []):
#        create_tree(child, current_node)
#    return current_node
#
## Create the tree from the root
#root = create_tree(data)
#
## Print the tree structure
#for pre, fill, node in RenderTree(root):
#    print(f"{pre}{node.name}")
#
## Export the tree to a LaTeX file
#latex_exporter = LatexExporter(root)
#latex_exporter.to_file("tree.tex")
#
## Display a message
#print("LaTeX file 'tree.tex' has been created.")



import json
from anytree import Node, RenderTree

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

# Function to generate LaTeX code for the tree
def generate_latex(node):
    latex_str = f"[{node.name}"
    for child in node.children:
        latex_str += generate_latex(child)
    latex_str += "]"
    return latex_str

# Generate the LaTeX code
latex_tree = generate_latex(root)

# Create the LaTeX document
latex_document = f"""
\\documentclass{{article}}
\\usepackage{{forest}}
\\begin{{document}}
\\section*{{Ecosystem Tree}}
\\begin{{forest}}
for tree={{grow=east, draw, rounded corners, node options={{align=left}}}}
{latex_tree}
\\end{{forest}}
\\end{{document}}
"""

# Write the LaTeX document to a file
with open('tree.tex', 'w') as file:
    file.write(latex_document)

print("LaTeX file 'tree.tex' has been created.")

