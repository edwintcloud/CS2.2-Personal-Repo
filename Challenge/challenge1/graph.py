from vertex import Vertex


class Graph:
    """ Graph Class
    A class demonstrating the essential facts and functionalities of graphs.
    """

    def __init__(self, file_name=None):
        """Initialize a graph object with an empty dictionary."""
        self.vertices = {}
        self.num_vertices = 0
        self.num_edges = 0
        self.type = "G"

        # if file_name specified, read in graph from file
        if file_name:
            self._read_from_file(file_name)

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return
        the vertex."""
        if key not in self.vertices:
            self.num_vertices += 1
            self.vertices[key] = Vertex(key)
        return self.vertices[key]

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        return None if key not in self.vertices else self.vertices[key]

    def add_edge(self, key1, key2, weight=1):
        """Add an edge from vertex with key `key1` to vertex with key `key2`
        with an optional weight."""
        if self.get_vertex(key1) is None:
            self.add_vertex(key1)
        if self.get_vertex(key2) is None:
            self.add_vertex(key2)
        self.num_edges += 1
        self.vertices[key1].add_neighbor(self.vertices[key2], weight)

    def get_vertices(self):
        """Return all the vertices in the graph."""
        return self.vertices.keys()

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v
        in g."""
        return iter(self.vertices.values())

    def get_edges(self):
        """Return a list of edges in the graph."""
        result = []
        for v in self.vertices.values():
            for w in v.neighbors:
                result.append((v.get_id(), w.get_id(), v.get_edge_weight(w)))
        return result

    def _read_from_file(self, file_name):
        """Read a graph from a file."""

        # load file specified
        with open(file_name, 'r') as f:
            file_lines = f.readlines()

        # if less than 3 lines in file, throw error
        if len(file_lines) < 3:
            raise Exception("Expected input file to contain at least 3 lines.")

        # set graph type
        self.type = file_lines[0].strip()
        if self.type != "G" and self.type != "D":
            raise Exception(
                f"Expected input file to have a type of G or D for line 1 \
                    but {self.type} was given."
            )

        # add graph vertices
        for vtx in file_lines[1].strip().split(','):
            self.add_vertex(vtx)

        # add graph edges
        for line in file_lines[2:]:
            edge_spec = line.strip("() \n").split(',')
            if len(edge_spec) != 3 and len(edge_spec) != 2:
                raise Exception(
                    f"Expected input file edge specification to have 2 or 3 \
                        items but {line} was given."
                )
            vtx1, vtx2 = edge_spec[:2]
            weight = 1 if len(edge_spec) != 3 else int(edge_spec[2])
            if self.type == "G":
                self.add_edge(vtx1, vtx2, weight)
                self.add_edge(vtx2, vtx1, weight)
            else:
                self.add_edge(vtx1, vtx2, weight)
