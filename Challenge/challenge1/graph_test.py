import unittest
from graph import Graph
from vertex import Vertex


class GraphTest(unittest.TestCase):

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("apple")
        graph.add_vertex("banana")

        self.assertEqual(2, graph.num_vertices)
        self.assertIsInstance(graph.get_vertex("apple"), Vertex)

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex("apple")
        graph.add_vertex("banana")
        graph.add_vertex("coconut")

        graph.add_edge("apple", "banana")
        graph.add_edge("apple", "coconut", 3)

        self.assertEqual(3, graph.num_vertices)
        self.assertEqual(2, graph.num_edges)

        graph.add_edge("pineapple", "strawberry")

        self.assertEqual(5, graph.num_vertices)
        self.assertEqual(3, graph.num_edges)
        self.assertCountEqual(
            ["apple", "banana", "coconut", "pineapple", "strawberry"],
            graph.get_vertices())

    def test_input_type_incorrect(self):
        self.assertRaisesRegex(
            Exception, "Expected input file to have a type of G or D for line 1", Graph,
            "test_inputs/type_incorrect.txt")

    def test_empty_file(self):
        self.assertRaisesRegex(
            Exception, "Expected input file to contain at least 3 lines", Graph,
            "test_inputs/empty.txt")

    def test_edge_incorrect(self):
        self.assertRaisesRegex(
            Exception, "Expected input file edge specification to have 2 or 3 items", Graph,
            "test_inputs/edge_incorrect.txt")

    def test_basic_input(self):
        result_graph = Graph("test_inputs/simple.txt")
        self.assertEqual(4, result_graph.num_vertices)
        self.assertCountEqual(
            result_graph.get_vertices(),
            ['1', '2', '3', '4'])

        self.assertEqual(6, result_graph.num_edges)
        self.assertCountEqual(
            [('1', '2', 1), ('1', '3', 1), ('2', '1', 1),
             ('2', '4', 1), ('3', '1', 1), ('4', '2', 1)],
            result_graph.get_edges())

    def test_extra_vertex(self):
        result_graph = Graph("test_inputs/extra_vertex.txt")
        self.assertEqual(5, result_graph.num_vertices)
        self.assertCountEqual(
            result_graph.get_vertices(),
            ['1', '2', '3', '4', '6'])

        self.assertEqual(4, result_graph.num_edges)
        self.assertCountEqual(
            [('1', '2', 1), ('1', '3', 1),
             ('2', '4', 1), ('2', '6', 1)],
            result_graph.get_edges())

    def test_unused_vertex(self):
        result_graph = Graph("test_inputs/unused_vertex.txt")
        self.assertEqual(5, result_graph.num_vertices)
        self.assertCountEqual(
            result_graph.get_vertices(),
            ['1', '2', '3', '4', '5'])

        self.assertEqual(4, result_graph.num_edges)
        self.assertCountEqual(
            [('1', '2', 1), ('1', '4', 1),
             ('2', '3', 1), ('3', '1', 1)],
            result_graph.get_edges())

    def test_weighted(self):
        result_graph = Graph("test_inputs/weighted.txt")
        self.assertEqual(5, result_graph.num_vertices)
        self.assertCountEqual(
            result_graph.get_vertices(),
            ['1', '6', '10', '15', '21'])

        self.assertEqual(6, result_graph.num_edges)
        self.assertCountEqual(
            [
                ('1', '6', 9),
                ('6', '10', 4),
                ('6', '15', 2),
                ('21', '10', 3),
                ('15', '1', 10),
                ('1', '21', 5)
            ],
            result_graph.get_edges())


if __name__ == "__main__":
    unittest.main()
