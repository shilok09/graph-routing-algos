import random
from src.graph_utils import Graph


def generate_sparse_graph(num_vertices: int, directed: bool = True) -> Graph:
    graph = Graph(num_vertices, directed=directed)
    
    # Add approximately V edges
    num_edges = num_vertices - 1
    edges_added = 0
    
    while edges_added < num_edges:
        u = random.randint(1, num_vertices)
        v = random.randint(1, num_vertices)
        
        if u != v:
            weight = random.randint(1, 100)
            # Check if edge doesn't already exist
            if not any(neighbor == v for neighbor, _ in graph.adj_list[u]):
                graph.add_edge(u, v, weight)
                edges_added += 1
    
    return graph


def generate_dense_graph(num_vertices: int, directed: bool = True) -> Graph:
    graph = Graph(num_vertices, directed=directed)
    
    # Add edges between most pairs
    for u in range(1, num_vertices + 1):
        for v in range(1, num_vertices + 1):
            if u != v and random.random() < 0.7:  # 70% probability of edge
                weight = random.randint(1, 100)
                graph.add_edge(u, v, weight)
    
    return graph


def generate_mixed_graph(num_vertices: int, directed: bool = True, include_negatives: bool = True) -> Graph:
    graph = Graph(num_vertices, directed=directed)
    
    num_edges = int(num_vertices * 1.5)
    edges_added = 0
    
    while edges_added < num_edges:
        u = random.randint(1, num_vertices)
        v = random.randint(1, num_vertices)
        
        if u != v:
            if include_negatives:
                weight = random.randint(-50, 100)
            else:
                weight = random.randint(1, 100)
            
            # Check if edge doesn't already exist
            if not any(neighbor == v for neighbor, _ in graph.adj_list[u]):
                graph.add_edge(u, v, weight)
                edges_added += 1
    
    return graph


def generate_complete_graph(num_vertices: int, directed: bool = True) -> Graph:
    graph = Graph(num_vertices, directed=directed)
    
    for u in range(1, num_vertices + 1):
        for v in range(1, num_vertices + 1):
            if u != v:
                weight = random.randint(1, 100)
                graph.add_edge(u, v, weight)
    
    return graph


def generate_bipartite_graph(num_vertices_per_side: int) -> Graph:
    graph = Graph(num_vertices_per_side * 2, directed=True)
    
    # First side: vertices 1 to num_vertices_per_side
    # Second side: vertices num_vertices_per_side+1 to 2*num_vertices_per_side
    
    for u in range(1, num_vertices_per_side + 1):
        for v in range(num_vertices_per_side + 1, 2 * num_vertices_per_side + 1):
            if random.random() < 0.6:
                weight = random.randint(1, 100)
                graph.add_edge(u, v, weight)
    
    return graph


def generate_grid_graph(grid_size: int) -> Graph:
    num_vertices = grid_size * grid_size
    graph = Graph(num_vertices, directed=False)
    
    # Connect adjacent vertices in grid
    for i in range(grid_size):
        for j in range(grid_size):
            current = i * grid_size + j + 1
            
            # Right neighbor
            if j < grid_size - 1:
                right = i * grid_size + (j + 1) + 1
                weight = random.randint(1, 10)
                graph.add_edge(current, right, weight)
            
            # Bottom neighbor
            if i < grid_size - 1:
                bottom = (i + 1) * grid_size + j + 1
                weight = random.randint(1, 10)
                graph.add_edge(current, bottom, weight)
    
    return graph


# Test graph generation
if __name__ == "__main__":
    print("Testing Graph Generation\n")
    
    # Sparse graph
    print("=== Sparse Graph (10 vertices) ===")
    sparse = generate_sparse_graph(10)
    sparse.print_graph()
    
    # Dense graph
    print("\n=== Dense Graph (5 vertices) ===")
    dense = generate_dense_graph(5)
    dense.print_graph()
    
    # Mixed graph
    print("\n=== Mixed Graph (6 vertices, with negatives) ===")
    mixed = generate_mixed_graph(6, include_negatives=True)
    mixed.print_graph()
