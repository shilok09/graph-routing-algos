# Algorithm Explanations

## Overview
This project implements four classical shortest path algorithms used in graph routing and network optimization problems. Each algorithm has different strengths depending on graph characteristics and requirements.

---

## 1. Dijkstra's Algorithm

### Description
Dijkstra's algorithm finds the shortest path from a single source vertex to all other vertices in a graph with **non-negative weights**.

### Time Complexity
- **With Min-Heap**: O((V + E) log V)
- **With Fibonacci Heap**: O(E + V log V)

### Space Complexity
O(V)

### Algorithm Steps
1. Initialize distances to all vertices as infinity, except source (0)
2. Use a min-heap priority queue to always process the closest unvisited vertex
3. For each vertex, relax all outgoing edges
4. Continue until all vertices are visited or queue is empty

### Advantages
- Fast for sparse graphs
- Optimal for non-negative weights
- Efficient with min-heap implementation

### Disadvantages
- Cannot handle negative weights
- Not suitable for all-pairs shortest paths (requires running once per source)

### When to Use
- Finding shortest route in navigation systems
- Network routing protocols
- Single-source shortest path problems with non-negative weights

### Example
```
Graph: 1--2(2)--4(7)--5(1)
       |         /
       3(4)--5(3)

From source 1:
- Distance to 1: 0
- Distance to 2: 2
- Distance to 3: 3
- Distance to 4: 9
- Distance to 5: 6 (via 1->3->5)
```

---

## 2. Bellman-Ford Algorithm

### Description
Bellman-Ford finds shortest paths from a single source and can handle **negative weights**. It can also **detect negative cycles**.

### Time Complexity
O(V × E)

### Space Complexity
O(V)

### Algorithm Steps
1. Initialize distances to all vertices as infinity, except source (0)
2. Relax all edges V-1 times (where V is number of vertices)
3. After V-1 iterations, check for negative cycles by trying to relax edges once more
4. If any distance decreases, a negative cycle exists

### Advantages
- Handles negative weights
- Detects negative cycles
- Works on any graph with finite weights

### Disadvantages
- Slower than Dijkstra (O(VE) vs O((V+E)log V))
- Not efficient for large sparse graphs
- Not suitable for dense graphs

### When to Use
- Currency exchange arbitrage detection
- Graphs with negative weights but no negative cycles
- When negative cycle detection is needed
- Distributed routing systems

### Example
```
Graph with negative weights:
1--2(-1)--4(2)
|         /
3(4)--5(-5)

From source 1:
- Distance to 1: 0
- Distance to 2: -1
- Distance to 3: 2 (via shortest path)
- Distance to 4: 0
```

---

## 3. Floyd-Warshall Algorithm

### Description
Floyd-Warshall computes shortest paths between **all pairs of vertices** in a graph. Works with negative weights and detects negative cycles.

### Time Complexity
O(V³)

### Space Complexity
O(V²) - requires distance matrix

### Algorithm Steps
1. Initialize distance matrix with edge weights (infinity for non-adjacent vertices)
2. For each intermediate vertex k (1 to V):
   - For each pair (i, j):
     - dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
3. Check diagonal elements - if any < 0, negative cycle exists

### Advantages
- Computes all-pairs shortest paths
- Handles negative weights
- Simple to implement
- Detects negative cycles

### Disadvantages
- O(V³) time complexity - very slow for large graphs
- Requires O(V²) space
- Not efficient for sparse graphs
- Much slower than Dijkstra run V times for sparse graphs

### When to Use
- Complete distance matrices needed
- Small to medium-sized graphs (V < 500)
- Graphs with negative weights
- Computing diameter of graph
- Transitive closure computation

### Example
```
3-vertex graph:
Distance Matrix (initial):
  1  2  3
1 0  1  10
2 ∞  0  2
3 ∞  ∞  0

After Floyd-Warshall:
  1  2  3
1 0  1  3    (1->2->3 is shorter than 1->3)
2 ∞  0  2
3 ∞  ∞  0
```

---

## 4. Johnson's Algorithm

### Description
Johnson's algorithm computes shortest paths between **all pairs** efficiently using a combination of Bellman-Ford and Dijkstra. Optimized for sparse graphs.

### Time Complexity
O(V² log V + VE)

### Space Complexity
O(V²) for distance matrix

### Algorithm Steps
1. Add auxiliary vertex with weight-0 edges to all other vertices
2. Run Bellman-Ford from auxiliary vertex to get potentials h(v)
3. Re-weight edges: w'(u,v) = w(u,v) + h(u) - h(v)
4. Run Dijkstra from each vertex using re-weighted edges
5. Convert distances back to original weights

### Advantages
- More efficient than Floyd-Warshall for sparse graphs
- Handles negative weights
- Detects negative cycles
- Better than running Dijkstra V times for sparse graphs

### Disadvantages
- Complex to implement
- More overhead than Floyd-Warshall for small dense graphs
- Requires re-weighting step

### When to Use
- All-pairs shortest paths in sparse graphs
- Large sparse graphs (V > 100)
- When negative weights are present
- Better alternative to Floyd-Warshall for sparse networks

### Example
```
Same as Floyd-Warshall but computed more efficiently
using combination of Bellman-Ford + Dijkstra
```

---

## Comparison Table

| Feature | Dijkstra | Bellman-Ford | Floyd-Warshall | Johnson |
|---------|----------|--------------|----------------|---------|
| Shortest Path Type | Single-source | Single-source | All-pairs | All-pairs |
| Negative Weights | ✗ | ✓ | ✓ | ✓ |
| Negative Cycle Detection | - | ✓ | ✓ | ✓ |
| Time Complexity | O((V+E)logV) | O(VE) | O(V³) | O(V²logV+VE) |
| Space Complexity | O(V) | O(V) | O(V²) | O(V²) |
| Best For | Sparse, non-negative | Any weights | Dense, small graphs | Sparse, any weights |
| Implementation | Simple | Simple | Simple | Complex |

---

## When to Choose Which Algorithm

### Use Dijkstra if:
- Graph has **only non-negative weights**
- You need **single-source** shortest paths
- Graph is **sparse**
- You want the **fastest algorithm** for this scenario

### Use Bellman-Ford if:
- Graph has **negative weights** but **no negative cycles**
- You need **single-source** shortest paths
- You need to **detect negative cycles**
- Graph is small to medium-sized

### Use Floyd-Warshall if:
- You need **all-pairs shortest paths**
- Graph is **small to medium-sized** (V < 500)
- Graph is **dense**
- You need **simple implementation**

### Use Johnson's if:
- You need **all-pairs shortest paths**
- Graph is **sparse and large**
- Graph has **negative weights** but **no negative cycles**
- You want **better performance** than Floyd-Warshall for sparse graphs

---

## Real-World Applications

### Dijkstra
- GPS Navigation (Google Maps, Waze)
- Network routing (OSPF protocol)
- Social networks (finding shortest connection)

### Bellman-Ford
- Currency arbitrage detection
- Bitcoin cryptocurrency exchanges
- Distributed routing protocols (RIP)

### Floyd-Warshall
- Network routing matrix computation
- Game pathfinding (smaller game worlds)
- Transitive closure computation

### Johnson
- Large-scale network analysis
- Internet topology analysis
- Large sparse social network analysis
