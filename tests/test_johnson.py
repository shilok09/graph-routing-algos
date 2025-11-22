import unittest
from src.graph_utils import Graph
from src.algorithms.johnson import johnson

INF = float('inf')


class TestJohnson(unittest.TestCase):
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
        
        # Small graph
        self.graph4 = Graph(3)
        self.graph4.add_edge(1, 2, 1)
        self.graph4.add_edge(2, 3, 2)
        self.graph4.add_edge(1, 3, 10)
    
    def test_positive_weights(self):
       
        dist, _, has_cycle = johnson(self.graph1)
        
        self.assertFalse(has_cycle)
        if dist is not None:
            self.assertEqual(dist[1][1], 0)
            self.assertEqual(dist[1][2], 2)
            self.assertEqual(dist[1][3], 3)
    
    def test_shortest_path_finding(self):
       
        dist, _, _ = johnson(self.graph4)
        
        if dist is not None:
            # Shortest path from 1 to 3 should be 1->2->3 = 3, not direct 1->3 = 10
            self.assertEqual(dist[1][3], 3)
    
    def test_negative_weights_no_cycle(self):
        
        dist, _, has_cycle = johnson(self.graph2)
        
        self.assertFalse(has_cycle)
        if dist is not None:
            self.assertEqual(dist[1][1], 0)
            self.assertEqual(dist[1][2], -1)
    
    def test_negative_cycle_detection(self):
      
        dist, _, has_cycle = johnson(self.graph3)
        
        self.assertTrue(has_cycle)
        self.assertIsNone(dist)
    
    def test_all_pairs_computed(self):
       
        dist, _, has_cycle = johnson(self.graph1)
        
        if not has_cycle and dist is not None:
            # Check that all entries are computed
            for i in range(1, 6):
                for j in range(1, 6):
                    self.assertTrue(dist[i][j] >= 0 or dist[i][j] == INF)
    
    def test_diagonal_elements_zero(self):
        
        dist, _, has_cycle = johnson(self.graph1)
        
        if not has_cycle and dist is not None:
            for i in range(1, 6):
                self.assertEqual(dist[i][i], 0)
    
    def test_relaxations_count(self):
       
        _, relaxations, _ = johnson(self.graph1)
        
        self.assertGreater(relaxations, 0)
    
    def test_vs_floyd_warshall(self):
        
        from src.algorithms.floyd_warshall import floyd_warshall
        
        fw_dist, _, fw_cycle = floyd_warshall(self.graph1)
        j_dist, _, j_cycle = johnson(self.graph1)
        
        self.assertEqual(fw_cycle, j_cycle)
        
        if not fw_cycle and j_dist is not None:
            # Compare results
            for i in range(1, 6):
                for j in range(1, 6):
                    # Allow small floating point differences
                    self.assertAlmostEqual(fw_dist[i][j], j_dist[i][j], places=5)


if __name__ == '__main__':
    unittest.main()
