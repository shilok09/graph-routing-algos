import heapq
from typing import Dict, List, Tuple

INF = float('inf')


def bellman_ford_johnson(graph, source: int) -> Tuple[Dict[int, float], bool]:
    distances = {i: INF for i in graph.vertices}
    distances[source] = 0
    
    for _ in range(graph.num_vertices - 1):
        for u, v, weight in graph.edges:
            if distances[u] != INF and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative cycles
    has_negative_cycle = False
    for u, v, weight in graph.edges:
        if distances[u] != INF and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break
    
    return distances, has_negative_cycle


def dijkstra_johnson(graph, source: int, h: Dict[int, float]) -> Tuple[Dict[int, float], int]:
    distances = {i: INF for i in graph.vertices}
    distances[source] = 0
    
    pq = [(0, source)]
    visited = set()
    relaxations = 0
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        
        visited.add(u)
        
        if u in graph.adj_list:
            for v, weight in graph.adj_list[u]:
                if v not in visited:
                    # Re-weighted edge: w'(u,v) = w(u,v) + h(u) - h(v)
                    adjusted_weight = weight + h[u] - h[v]
                    new_dist = current_dist + adjusted_weight
                    
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        relaxations += 1
                        heapq.heappush(pq, (new_dist, v))
    
    return distances, relaxations


def johnson(graph) -> Tuple[List[List[float]], int, bool]:
    n = graph.num_vertices
    relaxations = 0
    
    # Step 1: Add auxiliary vertex (vertex 0) with edges to all vertices
    # with weight 0
    original_edges = graph.edges.copy()
    original_adj = dict(graph.adj_list)
    
    for v in graph.vertices:
        graph.add_edge(0, v, 0)
    graph.num_vertices += 1
    graph.vertices.insert(0, 0)
    
    # Step 2: Run Bellman-Ford from auxiliary vertex
    h, has_negative_cycle = bellman_ford_johnson(graph, 0)
    
    if has_negative_cycle:
        # Restore original graph state before returning
        graph.num_vertices -= 1
        graph.vertices = graph.vertices[1:]
        graph.edges = original_edges
        graph.adj_list = original_adj
        return None, relaxations, True
    
    # Step 3: No need to mutate edges; we'll apply re-weighting on the fly in Dijkstra
    graph.edges = original_edges
    
    # Step 4: Run Dijkstra from each vertex
    dist_matrix = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for s in graph.vertices[1:]:  # Skip auxiliary vertex
        dijkstra_dist, rel = dijkstra_johnson(graph, s, h)
        
        # Restore original distances
        for v in graph.vertices[1:]:
            if dijkstra_dist[v] != INF:
                dist_matrix[s][v] = dijkstra_dist[v] + h[v] - h[s]
            else:
                dist_matrix[s][v] = INF
        dist_matrix[s][s] = 0
        
        relaxations += rel
    
    # Restore original graph state
    graph.num_vertices -= 1
    graph.vertices = graph.vertices[1:]
    graph.edges = original_edges
    graph.adj_list = original_adj
    
    return dist_matrix, relaxations, False


def print_distance_matrix(dist: List[List[float]], num_vertices: int, has_negative_cycle: bool = False) -> None:
    print(f"\nAll-Pairs Shortest Paths (Johnson's Algorithm):")
    
    if has_negative_cycle:
        print("⚠️  WARNING: Negative cycle detected in graph!")
        print("Algorithm cannot compute results.\n")
        return
    
    print(f"Distance Matrix ({num_vertices}x{num_vertices}):")
    
    # Print header
    print("     ", end="")
    for j in range(1, num_vertices + 1):
        print(f"{j:8}", end="")
    print()
    
    # Print rows
    for i in range(1, num_vertices + 1):
        print(f"{i:4}: ", end="")
        for j in range(1, num_vertices + 1):
            val = dist[i][j]
            if val == INF:
                print(f"{'INF':8}", end="")
            else:
                print(f"{int(val) if val == int(val) else val:8.1f}", end="")
        print()
    print()


def print_specific_distances(dist: List[List[float]], source: int, num_vertices: int) -> None:
    print(f"\nShortest Paths from Source {source}:")
    print(f"{'Vertex':<10} {'Distance':<15}")
    print("-" * 25)
    
    for j in range(1, num_vertices + 1):
        distance = dist[source][j]
        if distance == INF:
            print(f"{j:<10} {'INF':<15}")
        else:
            print(f"{j:<10} {int(distance) if distance == int(distance) else distance:<15}")
    print()
