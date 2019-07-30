#!python

import sys
from graph import Graph

if __name__ == "__main__":

    # get args
    f_name = sys.argv[1]
    vtx_A = sys.argv[2]
    vtx_B = sys.argv[3]

    # create graph
    g = Graph(f_name)

    # try recursive dfs from vtx_A to vtx_B
    result = g.find_path(vtx_A, vtx_B)
    result_string = ",".join(result)
    result_bool = len(result) > 0

    # print if there is a path
    print(
        'There exists a path between vertex {} and {}: {}'.format(
            vtx_A, vtx_B, result_bool
        )
    )
    print(f"Vertices in the path: {result_string}")
