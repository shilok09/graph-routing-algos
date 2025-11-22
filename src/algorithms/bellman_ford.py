from typing import Dict, Tuple

INF = float('inf')


def bellman_ford(graph, source: int) -> Tuple[Dict[int, float], int, bool]:
    distances = {i: INF for i in graph.vertices}
    distances[source] = 0
    relaxations = 0
    
    # Relax edges V-1 times
    for _ in range(graph.num_vertices - 1):
        for u, v, weight in graph.edges:
            if distances[u] != INF and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                relaxations += 1
    
    # Check for negative cycles
    has_negative_cycle = False
    for u, v, weight in graph.edges:
        if distances[u] != INF and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break
    
    return distances, relaxations, has_negative_cycle


def print_distances(distances: Dict[int, float], source: int, has_negative_cycle: bool = False) -> None:
    print(f"\nShortest Paths from Source {source} (Bellman-Ford):")
    
    if has_negative_cycle:
        print("⚠️  WARNING: Negative cycle detected in graph!")
        print("Results may be unreliable.\n")
    
    print(f"{'Vertex':<10} {'Distance':<15}")
    print("-" * 25)
    
    for vertex in sorted(distances.keys()):
        dist = distances[vertex]
        if dist == INF:
            print(f"{vertex:<10} {'INF':<15}")
        else:
            print(f"{vertex:<10} {int(dist) if dist == int(dist) else dist:<15}")
    print()
