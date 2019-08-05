from vertex import Vertex
import random
from queue import SimpleQueue, PriorityQueue
from collections import defaultdict


class Graph(object):
    """
    A graph object representation.
    """

    def __init__(self, file_name=None):
        """
        Initialize a graph object.

        Args:
            file_name (string): The file name or file path to read in
            a graph from.

        Returns:
            (Graph): The initialized graph object.
        """
        self.vertices = {}
        self.num_vertices = 0
        self.num_edges = 0
        self.type = "G"

        # if file_name specified, read in graph from file
        if file_name:
            self._read_from_file(file_name)

    def add_vertex(self, id):
        """
        Add a vertex to the graph by id and return the created vertex object.

        Args:
            id (any): The id of the vertex to create.

        Returns:
            (Vertex): The vertex creatqed.
        """
        if id not in self.vertices:
            self.num_vertices += 1
            self.vertices[id] = Vertex(id)
        return self.vertices[id]

    def get_vertex(self, id):
        """
        Return a vertex by id.

        Args:
            id (any): The id of the vertex to return.

        Returns:
            (Vertex|None): The vertex by id or None if not exists.
        """
        return None if id not in self.vertices else self.vertices[id]

    def add_edge(self, vtx_A, vtx_B, weight=1):
        """
        Add an edge from a start vertex to an end vertex.

        Args:
            vtx_A (any): The start vertex in the edge.
            vtx_B (any): The end vertex in the edge.
            weight (any): The weight to be assigned to the edge.
        """
        if self.get_vertex(vtx_A) is None:
            self.add_vertex(vtx_A)
        if self.get_vertex(vtx_B) is None:
            self.add_vertex(vtx_B)
        self.num_edges += 1
        self.vertices[vtx_A].add_neighbor(self.vertices[vtx_B], weight)

    def get_vertices(self):
        """
        Return a list of vertices.

        Returns:
            ([string]): An list of vertices keys.
        """

        return self.vertices.keys()

    def __iter__(self):
        """
        Return an iterator to iterate over vertex values.

        Returns:
            (iterable): An iterator over vertices values.
        """
        return iter(self.vertices.values())

    def get_edges(self, weighted=False):
        """
        Return a list of edges in the graph.

        Args:
            weighted (bool): if True, resulting list will also contain the
            edge weights
        """
        result = []
        for v in self.vertices.values():
            for w in v.neighbors:
                if weighted:
                    result.append(
                        (v.get_id(), w.get_id(), v.get_edge_weight(w))
                    )
                else:
                    result.append((v.get_id(), w.get_id()))
        return result

    def find_path(self, vtx_A, vtx_B):
        """
        Use dfs to determine if a path exists from vtx_A to vtx_B.

        Args:
            vtx_A (any): The start vertex.
            vtx_B (any): The end vertex.

        Returns:
            result ([any]): List of vertex ids in order of traversal.

        Raises:
            Exception: If vtx_A or vtx_B not in graph.
        """

        # ensure that vtxA and vtxB are in graph
        if vtx_A not in self.vertices or vtx_B not in self.vertices:
            raise Exception(
                f"One or both of the supplied vertices {vtx_A}, {vtx_B} \
                is not in this graph."
            )

        # create our needed structures
        path = []
        visited = set()

        # define recursive dfs
        def dfs(vtx):
            if vtx not in visited and self.vertices[vtx_B] not in visited:
                path.append(vtx.id)
                visited.add(vtx)
                for neighbor in vtx.get_neighbors():
                    dfs(neighbor)
            return path

        # call dfs starting with vtx_A
        dfs_path = dfs(self.vertices[vtx_A])

        # if the last element in the path is not vtx_B,
        # there is no path to vtx_B, return []
        if dfs_path[-1] != vtx_B:
            return []

        # otherwise return the dfs path
        return dfs_path

    def prims(self):
        start_vtx = random.choice(list(self.vertices.keys()))
        mst = defaultdict(set)
        visited = set([start_vtx])
        pq = PriorityQueue()

        # initialize pq
        for neighbor, weight in self.vertices[start_vtx].neighbors.items():
            pq.put((weight, start_vtx, neighbor.id))

        while pq.qsize() > 0:
            _, vtx_A, vtx_B = pq.get()
            if vtx_B not in visited:
                visited.add(vtx_B)
                mst[vtx_A].add(vtx_B)
                for neighbor, weight in self.vertices[vtx_B].neighbors.items():
                    if neighbor.id not in visited:
                        pq.put((weight, vtx_B, neighbor.id))
        return mst

    def dijkstra(self, start_vtx):
        distances = {v: float('inf') for v in self.vertices}
        distances[start_vtx] = 0
        pq = PriorityQueue()
        pq.put((0, start_vtx))

        while pq.qsize() > 0:
            cur_dist, cur_vtx = pq.get()

            if cur_dist > distances[cur_vtx]:
                continue

            for neighbor, weight in self.vertices[cur_vtx].neighbors.items():
                dist = cur_dist + weight

                if dist < distances[neighbor.id]:
                    distances[neighbor.id] = dist
                    pq.put((dist, neighbor.id))

        return distances

    def _read_from_file(self, file_name):
        """
        Read a graph from a file.

        Args:
            vtx_A (string): The file name or file path to read from.

        Raises:
            Exception: If input file is improperly formatted.
        """

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
