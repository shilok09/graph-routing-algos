import unittest
from src.graph_utils import Graph
from src.algorithms.dijkstra import dijkstra

INF = float('inf')


class TestDijkstra(unittest.TestCase):

    
    def setUp(self):
       
        # Simple graph: 1->2(2), 1->3(4), 2->3(1), 2->4(7), 3->5(3), 4->5(1), 5->4(2)
        self.graph1 = Graph(5)
        edges1 = [(1, 2, 2), (1, 3, 4), (2, 3, 1), (2, 4, 7), (3, 5, 3), (4, 5, 1), (5, 4, 2)]
        for u, v, w in edges1:
            self.graph1.add_edge(u, v, w)
        
        # Single vertex
        self.graph2 = Graph(1)
        
        # Disconnected graph
        self.graph3 = Graph(4)
        self.graph3.add_edge(1, 2, 5)
        self.graph3.add_edge(3, 4, 3)
    
    def test_simple_graph(self):
        
        distances, _ = dijkstra(self.graph1, 1)
        
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 2)
        self.assertEqual(distances[3], 3)
        # Shortest path 1->2->3->5->4 has cost 2+1+3+2 = 8
        self.assertEqual(distances[4], 8)
        self.assertEqual(distances[5], 6)
    
    def test_from_different_source(self):
      
        distances, _ = dijkstra(self.graph1, 2)
        
        self.assertEqual(distances[2], 0)
        self.assertEqual(distances[3], 1)
        self.assertEqual(distances[4], 7)
        self.assertEqual(distances[5], 4)
    
    def test_single_vertex(self):
        distances, _ = dijkstra(self.graph2, 1)
        
        self.assertEqual(distances[1], 0)
    
    def test_disconnected_graph(self):
     
        distances, _ = dijkstra(self.graph3, 1)
        
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 5)
        self.assertEqual(distances[3], INF)
        self.assertEqual(distances[4], INF)
    
    def test_unreachable_vertex(self):
       
        distances, _ = dijkstra(self.graph3, 3)
        
        self.assertEqual(distances[3], 0)
        self.assertEqual(distances[4], 3)
        self.assertEqual(distances[1], INF)
        self.assertEqual(distances[2], INF)
    
    def test_all_distances_non_negative(self):
        
        distances, _ = dijkstra(self.graph1, 1)
        
        for v, d in distances.items():
            self.assertTrue(d >= 0 or d == INF)
    
    def test_relaxations_count(self):
       
        _, relaxations = dijkstra(self.graph1, 1)
        
        # Should have some relaxations for this graph
        self.assertGreater(relaxations, 0)


if __name__ == '__main__':
    unittest.main()
