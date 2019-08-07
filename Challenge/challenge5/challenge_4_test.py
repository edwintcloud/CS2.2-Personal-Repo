import unittest
from graph import Graph
from vertex import Vertex


class Chal3Test(unittest.TestCase):
    def test_is_eulerian_true(self):
        graph = Graph("test_inputs/graph_data.txt")
        result = graph.is_eulerian

        self.assertEqual(True, result)

    def test_is_eulerian_false(self):
        graph = Graph("test_inputs/not_eulerian.txt")
        result = graph.is_eulerian

        self.assertEqual(False, result)


if __name__ == "__main__":
    unittest.main()
