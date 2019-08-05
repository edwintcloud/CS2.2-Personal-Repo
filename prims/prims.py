#!python

import sys
from graph import Graph

if __name__ == "__main__":

    # get args
    f_name = sys.argv[1]

    # create graph
    g = Graph(f_name)

    # try recursive dfs from vtx_A to vtx_B
    result = g.prims()
    # try recursive dfs from vtx_A to vtx_B
    result2 = g.dijkstra('a')

    # print if there is a mst
    print('There exists a mst: {}'.format(result))

    print('Distances: {}'.format(result2))
