#!python

import sys
from graph import Graph

if __name__ == "__main__":

    # Create graph with specified file
    g = Graph(sys.argv[1])

    # The # vertices in the graph.
    print("# Vertices: {}".format(g.num_vertices))

    # The # edges in the graph.
    print("# Edges: {}".format(g.num_edges))

    # A list of the edges with their weights (if weighted)
    print("Edge List: ")
    for edge in g.get_edges():
        print("({},{},{})".format(*edge))
