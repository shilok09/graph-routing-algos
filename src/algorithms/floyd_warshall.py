from typing import List, Tuple

INF = float('inf')


def floyd_warshall(graph) -> Tuple[List[List[float]], int, bool]:
    n = graph.num_vertices
    dist = graph.get_adjacency_matrix()
    relaxations = 0
    
    # Three nested loops for Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] != INF and dist[k][j] != INF:
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist
                        relaxations += 1
    
    # Check for negative cycles (diagonal elements < 0)
    has_negative_cycle = False
    for i in range(1, n + 1):
        if dist[i][i] < 0:
            has_negative_cycle = True
            break
    
    return dist, relaxations, has_negative_cycle


def print_distance_matrix(dist: List[List[float]], num_vertices: int, has_negative_cycle: bool = False) -> None:
    print(f"\nAll-Pairs Shortest Paths (Floyd-Warshall):")
    
    if has_negative_cycle:
        print("⚠️  WARNING: Negative cycle detected in graph!")
        print("Results may be unreliable.\n")
    
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
