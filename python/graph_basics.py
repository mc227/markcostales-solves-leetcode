import networkx as nx

# instantiate a graph
G = nx.Graph()

# add edges

G.add_edges_from([(1,2),(2,3),(3,4),(4,1)])

# closest path from 1 to 3

path = nx.shortest_path(G,1,3)

print(path)




