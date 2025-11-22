"""
Unit tests for Floyd-Warshall Algorithm
"""

import unittest
from src.graph_utils import Graph
from src.algorithms.floyd_warshall import floyd_warshall

INF = float('inf')


class TestFloydWarshall(unittest.TestCase):
    """Test cases for Floyd-Warshall algorithm."""
    
    def setUp(self):
        """Set up test graphs."""
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
        """Test with positive weights."""
        dist, _, has_cycle = floyd_warshall(self.graph1)
        
        self.assertFalse(has_cycle)
        self.assertEqual(dist[1][1], 0)
        self.assertEqual(dist[1][2], 2)
        self.assertEqual(dist[1][3], 3)
    
    def test_shortest_path_finding(self):
        """Test that shortest paths are found correctly."""
        dist, _, _ = floyd_warshall(self.graph4)
        
        # Shortest path from 1 to 3 should be 1->2->3 = 3, not direct 1->3 = 10
        self.assertEqual(dist[1][3], 3)
    
    def test_negative_weights_no_cycle(self):
        """Test with negative weights but no cycle."""
        dist, _, has_cycle = floyd_warshall(self.graph2)
        
        self.assertFalse(has_cycle)
        self.assertEqual(dist[1][1], 0)
        self.assertEqual(dist[1][2], -1)
    
    def test_negative_cycle_detection(self):
        """Test negative cycle detection."""
        dist, _, has_cycle = floyd_warshall(self.graph3)
        
        self.assertTrue(has_cycle)
    
    def test_all_pairs_computed(self):
        """Test that all pairs have computed distances."""
        dist, _, _ = floyd_warshall(self.graph1)
        
        # Check that all entries are computed
        for i in range(1, 6):
            for j in range(1, 6):
                self.assertTrue(dist[i][j] >= 0 or dist[i][j] == INF)
    
    def test_diagonal_elements_zero(self):
        """Test that diagonal elements are zero (for no negative cycle)."""
        dist, _, has_cycle = floyd_warshall(self.graph1)
        
        if not has_cycle:
            for i in range(1, 6):
                self.assertEqual(dist[i][i], 0)
    
    def test_symmetry_in_undirected(self):
        """Test that distances are symmetric in undirected graph."""
        graph = Graph(3, directed=False)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 3)
        
        dist, _, _ = floyd_warshall(graph)
        
        # Should be symmetric
        self.assertEqual(dist[1][2], dist[2][1])
        self.assertEqual(dist[2][3], dist[3][2])
    
    def test_relaxations_count(self):
        """Test that relaxations are counted."""
        _, relaxations, _ = floyd_warshall(self.graph1)
        
        self.assertGreater(relaxations, 0)


if __name__ == '__main__':
    unittest.main()
