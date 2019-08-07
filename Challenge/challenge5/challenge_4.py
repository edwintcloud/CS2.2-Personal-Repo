#!python

import sys
from graph import Graph

if __name__ == "__main__":

    # get args
    f_name = sys.argv[1]

    # create graph
    g = Graph(f_name)

    # is graph Eulerian?
    print(f"This graph is Eulerian: {g.is_eulerian}")
