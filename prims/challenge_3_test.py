import unittest
from graph import Graph
from vertex import Vertex


class Chal3Test(unittest.TestCase):
    def test_find_path_valid(self):
        graph = Graph("test_inputs/graph_data.txt")
        result = graph.find_path("1", "5")

        self.assertEqual(['1', '2', '3', '5'], result)

    def test_find_path_invalid(self):
        graph = Graph("test_inputs/no_path.txt")
        result = graph.find_path("1", "5")

        self.assertEqual([], result)


if __name__ == "__main__":
    unittest.main()
