import unittest
from src.graph_utils import Graph
from src.algorithms.bellman_ford import bellman_ford

INF = float('inf')


class TestBellmanFord(unittest.TestCase):
   
    
    def setUp(self):
       
        # Graph with positive weights
        self.graph1 = Graph(5)
        edges1 = [(1, 2, 2), (1, 3, 4), (2, 3, 1), (2, 4, 7), (3, 5, 3), (4, 5, 1), (5, 4, 2)]
        for u, v, w in edges1:
            self.graph1.add_edge(u, v, w)
        
        # Graph with negative weights (no cycle)
        self.graph2 = Graph(4)
        self.graph2.add_edge(1, 2, -1)
        self.graph2.add_edge(1, 3, 4)
        self.graph2.add_edge(2, 3, 3)
        self.graph2.add_edge(2, 4, 2)
        self.graph2.add_edge(3, 4, -5)
        
        # Graph with negative cycle
        self.graph3 = Graph(3)
        self.graph3.add_edge(1, 2, 1)
        self.graph3.add_edge(2, 3, -3)
        self.graph3.add_edge(3, 1, 1)
        
        # Single vertex
        self.graph4 = Graph(1)
    
    def test_positive_weights(self):
       
        distances, _, has_cycle = bellman_ford(self.graph1, 1)
        
        self.assertFalse(has_cycle)
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 2)
        self.assertEqual(distances[3], 3)
    
    def test_negative_weights_no_cycle(self):
    
        distances, _, has_cycle = bellman_ford(self.graph2, 1)
        
        self.assertFalse(has_cycle)
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], -1)
        self.assertEqual(distances[3], 2)
        self.assertEqual(distances[4], 0)
    
    def test_negative_cycle_detection(self):
        
        distances, _, has_cycle = bellman_ford(self.graph3, 1)
        
        self.assertTrue(has_cycle)
    
    def test_single_vertex(self):
      
        distances, _, has_cycle = bellman_ford(self.graph4, 1)
        
        self.assertFalse(has_cycle)
        self.assertEqual(distances[1], 0)
    
    def test_from_different_source(self):
      
        distances, _, has_cycle = bellman_ford(self.graph1, 2)
        
        self.assertFalse(has_cycle)
        self.assertEqual(distances[2], 0)
        self.assertEqual(distances[3], 1)
        # Shortest path 2->3->5->4 has cost 1+3+2 = 6
        self.assertEqual(distances[4], 6)
    
    def test_relaxations_count(self):
       
        _, relaxations, _ = bellman_ford(self.graph1, 1)
        
        # Should have relaxations
        self.assertGreater(relaxations, 0)
    
    def test_negative_weights_reduce_distance(self):
       
        distances, _, has_cycle = bellman_ford(self.graph2, 1)
        
        # Distance to 4 should be reduced by negative edge
        self.assertLess(distances[4], distances[3] + 5)


if __name__ == '__main__':
    unittest.main()
