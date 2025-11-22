from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import sys

INF = float('inf')


class Graph:
       
    def __init__(self, num_vertices: int, directed: bool = True):
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list = defaultdict(list)  # adjacency list
        self.edges = []  # list of all edges (u, v, weight)
        self.vertices = list(range(1, num_vertices + 1))
    
    def add_edge(self, u: int, v: int, weight: float) -> None:
        self.adj_list[u].append((v, weight))
        self.edges.append((u, v, weight))
        
        if not self.directed:
            self.adj_list[v].append((u, weight))
            self.edges.append((v, u, weight))
    
    def get_adjacency_matrix(self) -> List[List[float]]:
        matrix = [[INF] * (self.num_vertices + 1) for _ in range(self.num_vertices + 1)]
        
        # Set diagonal to 0
        for i in range(self.num_vertices + 1):
            matrix[i][i] = 0
        
        # Fill in edge weights
        for u, v, weight in self.edges:
            if matrix[u][v] > weight:  # Keep minimum if duplicate edges
                matrix[u][v] = weight
        
        return matrix
    
    def get_adjacency_list(self) -> Dict[int, List[Tuple[int, float]]]:
        return dict(self.adj_list)
    
    def is_valid(self) -> bool:
        # Check all vertices are in valid range
        for u in self.adj_list:
            if u < 1 or u > self.num_vertices:
                return False
            for v, weight in self.adj_list[u]:
                if v < 1 or v > self.num_vertices:
                    return False
        return True
    
    def is_connected(self) -> bool:
        if not self.vertices:
            return True
        
        visited = set()
        
        def dfs(v):
            visited.add(v)
            for neighbor, _ in self.adj_list[v]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(self.vertices[0])
        return len(visited) == self.num_vertices
    
    def has_negative_cycle(self) -> bool:
        dist = [INF] * (self.num_vertices + 1)
        dist[1] = 0
        
        # Relax edges num_vertices - 1 times
        for _ in range(self.num_vertices - 1):
            for u, v, weight in self.edges:
                if dist[u] != INF and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        
        # Check for negative cycle
        for u, v, weight in self.edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                return True
        
        return False
    
    def print_graph(self) -> None:
        print(f"\nGraph ({self.num_vertices} vertices, {len(self.edges)} edges)")
        print(f"Directed: {self.directed}\n")
        print("Adjacency List:")
        for u in sorted(self.adj_list.keys()):
            neighbors = [f"{v}({w})" for v, w in sorted(self.adj_list[u])]
            print(f"  {u}: {' -> '.join(neighbors)}")
        print()
    
    def print_matrix(self) -> None:
        matrix = self.get_adjacency_matrix()
        print(f"\nAdjacency Matrix ({self.num_vertices}x{self.num_vertices}):")
        
        # Print header
        print("     ", end="")
        for j in range(1, self.num_vertices + 1):
            print(f"{j:8}", end="")
        print()
        
        # Print rows
        for i in range(1, self.num_vertices + 1):
            print(f"{i:4}: ", end="")
            for j in range(1, self.num_vertices + 1):
                val = matrix[i][j]
                if val == INF:
                    print(f"{'INF':8}", end="")
                else:
                    print(f"{int(val) if val == int(val) else val:8.1f}", end="")
            print()
        print()


def read_graph_from_file(filename: str) -> Graph:
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        # Parse first line
        parts = lines[0].strip().split()
        num_vertices = int(parts[0])
        num_edges = int(parts[1])
        
        graph = Graph(num_vertices, directed=True)
        
        # Parse edges
        for i in range(1, num_edges + 1):
            parts = lines[i].strip().split()
            u = int(parts[0])
            v = int(parts[1])
            weight = float(parts[2])
            graph.add_edge(u, v, weight)
        
        return graph
    
    except Exception as e:
        print(f"Error reading graph from file: {e}")
        return None


def write_graph_to_file(graph: Graph, filename: str) -> None:
    try:
        with open(filename, 'w') as f:
            f.write(f"{graph.num_vertices} {len(graph.edges)}\n")
            for u, v, weight in graph.edges:
                f.write(f"{u} {v} {weight}\n")
    except Exception as e:
        print(f"Error writing graph to file: {e}")


def create_sample_graphs() -> Dict[str, Graph]:
    graphs = {}
    
    # Sample Graph 1: Basic example from problem statement
    g1 = Graph(5, directed=True)
    edges = [(1, 2, 2), (1, 3, 4), (2, 3, 1), (2, 4, 7), (3, 5, 3), (4, 5, 1), (5, 4, 2)]
    for u, v, w in edges:
        g1.add_edge(u, v, w)
    graphs['sample'] = g1
    
    # Sample Graph 2: Disconnected graph
    g2 = Graph(6, directed=True)
    edges2 = [(1, 2, 1), (2, 3, 2), (4, 5, 1), (5, 6, 3)]
    for u, v, w in edges2:
        g2.add_edge(u, v, w)
    graphs['disconnected'] = g2
    
    # Sample Graph 3: With negative weights (no cycle)
    g3 = Graph(4, directed=True)
    edges3 = [(1, 2, -1), (1, 3, 4), (2, 3, 3), (2, 4, 2), (3, 4, -5)]
    for u, v, w in edges3:
        g3.add_edge(u, v, w)
    graphs['negative_weights'] = g3
    
    return graphs
