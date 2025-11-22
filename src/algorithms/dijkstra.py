import heapq
from typing import Dict, Tuple, List
from collections import defaultdict

INF = float('inf')


def dijkstra(graph, source: int) -> Tuple[Dict[int, float], int]:
    distances = {i: INF for i in graph.vertices}
    distances[source] = 0
    
    # Min heap: (distance, vertex)
    pq = [(0, source)]
    visited = set()
    relaxations = 0
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # Skip if already visited
        if u in visited:
            continue
        
        visited.add(u)
        
        # Check all neighbors
        if u in graph.adj_list:
            for v, weight in graph.adj_list[u]:
                if v not in visited:
                    new_dist = current_dist + weight
                    
                    # Relax edge
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        relaxations += 1
                        heapq.heappush(pq, (new_dist, v))
    
    return distances, relaxations


def print_distances(distances: Dict[int, float], source: int) -> None:
    print(f"\nShortest Paths from Source {source}:")
    print(f"{'Vertex':<10} {'Distance':<15}")
    print("-" * 25)
    
    for vertex in sorted(distances.keys()):
        dist = distances[vertex]
        if dist == INF:
            print(f"{vertex:<10} {'INF':<15}")
        else:
            print(f"{vertex:<10} {int(dist) if dist == int(dist) else dist:<15}")
    print()
