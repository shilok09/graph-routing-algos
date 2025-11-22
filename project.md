1. Problem Statement

Transportation, communication, and logistics networks rely on finding the most efficient paths between points.
This assignment explores various algorithms that solve the shortest path problem in graphs, determining the minimum cost or distance between nodes.

You are required to implement, test, and analyze the following shortest path algorithms:

Dijkstra’s Algorithm (Single Source, Non-negative weights)

Bellman-Ford Algorithm (Single Source, handles negative weights)

Floyd-Warshall Algorithm (All-Pairs, handles negative weights)

Johnson’s Algorithm (All-Pairs, handles negative weights efficiently)

2. Objectives

Understand and implement classical shortest path algorithms.

Compare algorithmic complexities and performances.

Analyze the behavior of algorithms under different graph conditions (dense/sparse, positive/negative weights).

Demonstrate the correctness of results with sample input/output.

3. Input Specifications

The input graph can be:

Directed or undirected

Represented as an adjacency matrix or edge list

Containing positive or negative weights (but no negative cycles)

Example Input Format:
5 7
1 2 2
1 3 4
2 3 1
2 4 7
3 5 3
4 5 1
5 4 2


Where:

5 → number of vertices

7 → number of edges

Next lines → u v w represents an edge from u → v with weight w

4. Output Specifications

The program should output:

For Dijkstra / Bellman-Ford:
The shortest distance from a given source vertex to all other vertices.

For Floyd-Warshall / Johnson:
A distance matrix representing the shortest path between all vertex pairs.

Example Output (for source = 1):
Vertex   Distance from Source
1        0
2        2
3        3
4        8
5        6

5. Implementation Requirements

Implement the following functions (in C++/Java/Python):

def dijkstra(graph, source):
    pass

def bellman_ford(graph, source):
    pass

def floyd_warshall(graph):
    pass

def johnson(graph):
    pass


You must:

Use adjacency list or adjacency matrix representation.

Handle disconnected graphs gracefully.

Detect and report negative weight cycles (for Bellman-Ford and Johnson).

6. Experimental Analysis

Perform experiments on three types of graphs:

Graph Type	No. of Vertices	Description
Sparse Graph	10–50	Few edges (E ≈ V)
Dense Graph	100–200	Many edges (E ≈ V²)
Mixed Graph	—	Random weights including negatives (For Bellman-Ford & Johnson)

For each case:

Record execution time, number of relaxations, and memory usage.

Compare the algorithms in a table or graph.


### FILE STRUCTURE:
├── data/
│   ├── sample_input.txt
│   ├── sample_output.txt
│   └── test_graphs/
│
├── src/
│   ├── main.py             
│   ├── graph_utils.py      # graph building, printing, validation
│   │
│   ├── algorithms/
│   │   ├── dijkstra.py
│   │   ├── bellman_ford.py
│   │   ├── floyd_warshall.py
│   │   └── johnson.py
│   │
│   └── analysis/
│       ├── benchmark.py        # timing, relaxations count, memory
│       ├── compare_algorithms.py
│       └── graph_generator.py  # create sparse/dense/random graphs
│
│
├── tests/
│   ├── test_dijkstra.py
│   ├── test_bellman_ford.py
│   ├── test_floyd_warshall.py
│   └── test_johnson.py
│
└── docs/
    ├── report.md
    ├── algorithm_explanations.md
    ├── experimental_results.md
    └── graphs/       