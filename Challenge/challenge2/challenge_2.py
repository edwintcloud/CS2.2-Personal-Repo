#!python

import sys
from graph import Graph

if __name__ == "__main__":

    # create graph with specified file
    g = Graph(sys.argv[1])

    # get the shortest path
    shortest_path = g.get_shortest_path(sys.argv[2], sys.argv[3])

    # the # vertices in the shortest path.
    print("Vertices in shortest path: {}".format(",".join(shortest_path)))

    # the # edges in the shortest path.
    print(
        "Number of edges in shortest path: {}".format(len(shortest_path) - 1)
    )
