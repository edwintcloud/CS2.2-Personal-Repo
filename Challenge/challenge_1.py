#!python

import sys

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.id} adjacent to {[x.id for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return iter(self.neighbors.keys())

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        return self.neighbors[vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.vertices = {}
        self.num_vertices = 0
        self.num_edges = 0

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        if key not in self.vertices:
            self.num_vertices += 1
            self.vertices[key] = Vertex(key)
        return self.vertices[key]

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        return None if key not in self.vertices else self.vertices[key]

    def add_edge(self, key1, key2, weight=0):
        """Add an edge from vertex with key `key1` to vertex with key `key2` with an optional weight."""
        if self.get_vertex(key1) is None:
            self.add_vertex(key1)
        if self.get_vertex(key2) is None:
            self.add_vertex(key2)
        self.num_edges += 1
        self.vertices[key1].add_neighbor(self.vertices[key2], weight)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertices.keys()

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vertices.values())


# Driver code


if __name__ == "__main__":

    # Load file specified in argv
    with open(sys.argv[1], 'r') as f:
        file_lines = f.readlines()

    # Create graph
    g = Graph()

    # Add vertices from file_lines[1]
    for vtx in file_lines[1].rstrip().split(','):
        g.add_vertex(vtx)

    # Add vertex connections from vertex pairs
    for vtx_pair in file_lines[2:]:
        vtx_pair_lst = vtx_pair.rstrip()[1:-1].split(',')
        if len(vtx_pair_lst) == 3:
            g.add_edge(vtx_pair_lst[0], vtx_pair_lst[1], vtx_pair_lst[2])
        else:
            g.add_edge(vtx_pair_lst[0], vtx_pair_lst[1])

    # The # vertices in the graph.
    print("# Vertices: {}".format(g.num_vertices))
    # The # edges in the graph.
    print("# Edges: {}".format(g.num_edges))

    # A list of the edges with their weights (if weighted)
    print("Edge List: ")
    for v in g:
        for w in v.get_neighbors():
            print("({},{},{})".format(v.get_id(),
                                      w.get_id(), v.get_edge_weight(w)))
