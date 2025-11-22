
================================================================================
ALGORITHM COMPARISON ANALYSIS
================================================================================

### BEST ALGORITHMS BY GRAPH TYPE ###

DENSE:
----------------------------------------
Fastest Algorithm: dijkstra
Average Time: 0.000671s

  Dense_10V:
    bellman_ford: 0.000000s, Relaxations: 25
    dijkstra: 0.000000s, Relaxations: 18
    floyd_warshall: 0.000996s, Relaxations: 157
    johnson: 0.000998s, Relaxations: 170

  Dense_25V:
    bellman_ford: 0.004357s, Relaxations: 86
    dijkstra: 0.001013s, Relaxations: 53
    floyd_warshall: 0.010995s, Relaxations: 1519
    johnson: 0.009993s, Relaxations: 1487

  Dense_50V:
    bellman_ford: 0.021992s, Relaxations: 248
    dijkstra: 0.001001s, Relaxations: 151
    floyd_warshall: 0.075591s, Relaxations: 10046
    johnson: 0.066326s, Relaxations: 7345

DENSE_100V:
----------------------------------------
Fastest Algorithm: dijkstra
Average Time: 0.004911s

  Dense_100V_Large:
    bellman_ford: 0.235609s, Relaxations: 572
    dijkstra: 0.004911s, Relaxations: 335
    floyd_warshall: 0.608842s, Relaxations: 54414
    johnson: 0.488164s, Relaxations: 35423

DENSE_200V:
----------------------------------------
Fastest Algorithm: dijkstra
Average Time: 0.009005s

  Dense_200V_Large:
    bellman_ford: 1.662910s, Relaxations: 1382
    dijkstra: 0.009005s, Relaxations: 792
    floyd_warshall: 3.659999s, Relaxations: 278558
    johnson: 3.252448s, Relaxations: 158421

MIXED:
----------------------------------------
Fastest Algorithm: dijkstra
Average Time: 0.000000s

  Mixed_10V:
    bellman_ford: FAILED - Negative cycle detected
    dijkstra: 0.000000s, Relaxations: 5
    floyd_warshall: FAILED - Negative cycle detected
    johnson: FAILED - Negative cycle detected

  Mixed_25V:
    bellman_ford: 0.000000s, Relaxations: 16
    dijkstra: 0.000000s, Relaxations: 17
    floyd_warshall: 0.004598s, Relaxations: 171
    johnson: 0.005991s, Relaxations: 228

  Mixed_50V:
    bellman_ford: FAILED - Negative cycle detected
    dijkstra: 0.000000s, Relaxations: 21
    floyd_warshall: FAILED - Negative cycle detected
    johnson: FAILED - Negative cycle detected

SPARSE:
----------------------------------------
Fastest Algorithm: dijkstra
Average Time: 0.000000s

  Sparse_10V:
    bellman_ford: 0.000000s, Relaxations: 0
    dijkstra: 0.000000s, Relaxations: 0
    floyd_warshall: 0.000000s, Relaxations: 8
    johnson: 0.000999s, Relaxations: 17

  Sparse_25V:
    bellman_ford: 0.000996s, Relaxations: 1
    dijkstra: 0.000000s, Relaxations: 1
    floyd_warshall: 0.005012s, Relaxations: 46
    johnson: 0.003898s, Relaxations: 68

  Sparse_50V:
    bellman_ford: 0.000000s, Relaxations: 0
    dijkstra: 0.000000s, Relaxations: 0
    floyd_warshall: 0.022381s, Relaxations: 304
    johnson: 0.006015s, Relaxations: 353

### ALGORITHM CHARACTERISTICS ###
----------------------------------------
Dijkstra:
  - Best for: Non-negative weights, single-source
  - Time: O((V+E)log V) with heap
  - Space: O(V)

Bellman-Ford:
  - Best for: Negative weights, single-source
  - Time: O(VE)
  - Can detect negative cycles

Floyd-Warshall:
  - Best for: All-pairs, small dense graphs
  - Time: O(V^3)
  - Space: O(V^2)

Johnson:
  - Best for: All-pairs sparse graphs
  - Time: O(V^2 log V + VE)
  - Better than Floyd-Warshall for sparse
