import graphviz

# Create the graph object
graph = graphviz.Graph()

# Add nodes
graph.node('A', 'Root')
graph.node('B', 'Left Child')
graph.node('C', 'Right Child')
graph.node('D', 'Left Grandchild')
graph.node('E', 'Right Grandchild')

# Add edges
graph.edge('A', 'B')
graph.edge('A', 'C')
graph.edge('B', 'D')
graph.edge('B', 'E')

# Render the graph
graph.render('heap_tree')
