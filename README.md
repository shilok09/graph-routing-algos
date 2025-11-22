# Shortest Path Algorithms - Complete Setup & Running Guide

## Project Structure

```
graph-routing-algos/
├── data/
│   ├── sample_input.txt
│   ├── sample_output.txt
│   └── test_graphs/
│       ├── negative_weights.txt
│       └── sparse_10v.txt
├── src/
│   ├── __init__.py
│   ├── main.py                          # Main entry point
│   ├── graph_utils.py                   # Graph building & utilities
│   ├── algorithms/
│   │   ├── __init__.py
│   │   ├── dijkstra.py                  # Dijkstra's Algorithm
│   │   ├── bellman_ford.py              # Bellman-Ford Algorithm
│   │   ├── floyd_warshall.py            # Floyd-Warshall Algorithm
│   │   └── johnson.py                   # Johnson's Algorithm
│   └── analysis/
│       ├── __init__.py
│       ├── benchmark.py                 # Performance benchmarking
│       ├── graph_generator.py           # Generate test graphs
│       └── compare_algorithms.py        # Algorithm comparison
├── tests/
│   ├── __init__.py
│   ├── test_dijkstra.py                 # Dijkstra tests
│   ├── test_bellman_ford.py             # Bellman-Ford tests
│   ├── test_floyd_warshall.py           # Floyd-Warshall tests
│   └── test_johnson.py                  # Johnson's tests
├── docs/
│   ├── algorithm_explanations.md        # Detailed algorithm info
│   ├── report.md                        # Main report
│   ├── experimental_results.md          # Benchmark results
│   └── graphs/                          # Result graphs
└── project.md                           # Project specification

```

---

## Prerequisites

Ensure you have Python 3.7+ installed. Check your version:

```bash
python --version
```

No external dependencies required - all algorithms use only Python standard library.

---

## How to Run

### Option 1: Interactive Menu (Recommended for Testing)

Navigate to the project root directory and run:

```bash
cd C:\Users\admin\Documents\AlgoAssignments\graph-routing-algos
python -m src.main
```

This opens an interactive menu with 7 options:

```
1. Load graph from file
   - Load a graph from data/ folder
   - Run any of the 4 algorithms on it
   - View results

2. Run specific algorithm on sample graph
   - Choose from 3 built-in sample graphs
   - Select algorithm (Dijkstra, Bellman-Ford, Floyd-Warshall, Johnson)
   - View detailed results with metrics

3. Compare all algorithms on sample graphs
   - Runs all 4 algorithms on each sample graph
   - Shows performance comparison table
   - Displays execution time, relaxations, memory usage

4. Run full comparison suite (sparse/dense/mixed)
   - Benchmarks all algorithms on different graph types
   - Sparse graphs: 10-50 vertices
   - Dense graphs: 10-50 vertices
   - Mixed graphs: With negative weights
   - Saves results to docs/experimental_results.md

5. Benchmark single algorithm
   - Profile individual algorithm performance
   - Detailed metrics for that algorithm

6. View sample graphs
   - Display all 3 built-in sample graphs
   - Shows adjacency list and matrix representation

7. Exit
   - Quit the program
```

### Option 2: Run Tests

Run all unit tests:

```bash
cd C:\Users\admin\Documents\AlgoAssignments\graph-routing-algos
python -m pytest tests/
```

Or run specific test file:

```bash
python -m pytest tests/test_dijkstra.py -v
python -m pytest tests/test_bellman_ford.py -v
python -m pytest tests/test_floyd_warshall.py -v
python -m pytest tests/test_johnson.py -v
```

If pytest is not installed, install it:

```bash
pip install pytest
```

Alternatively, run tests using unittest:

```bash
python -m unittest tests.test_dijkstra
python -m unittest tests.test_bellman_ford
python -m unittest tests.test_floyd_warshall
python -m unittest tests.test_johnson
```

### Option 3: Run Full Comparison Suite (Generates Report)

```bash
python -c "from src.analysis.compare_algorithms import run_full_comparison; run_full_comparison()"
```

This runs benchmarks on all graph types and generates a report at `docs/experimental_results.md`

---

## Quick Start Example

### Step 1: Navigate to Project Root
```powershell
cd C:\Users\admin\Documents\AlgoAssignments\graph-routing-algos
```

### Step 2: Start Interactive Menu
```powershell
python -m src.main
```

### Step 3: Try Option 2 (Run specific algorithm)
```
Select option: 2
Select graph: 1 (sample)
Select algorithm: 1 (Dijkstra)
Enter source vertex: 1
```

**Expected Output:**
```
Shortest Paths from Source 1:
Vertex     Distance
------     --------
1          0
2          2
3          3
4          9
5          6

Relaxations: 4
```

### Step 4: Compare All Algorithms (Option 3)
```
Select option: 3
```

**Shows comparison table:**
```
BENCHMARK COMPARISON TABLE
Test Name        Algorithm            Time (s)        Relaxations    Memory (KB)
sample           Dijkstra             0.000001        4              XX.XX
sample           Bellman-Ford         0.000002        6              XX.XX
...
```

---

## Algorithm Input/Output Formats

### Input Format (Graph File)

File format: `data/your_graph.txt`

```
5 7
1 2 2
1 3 4
2 3 1
2 4 7
3 5 3
4 5 1
5 4 2
```

Where:
- Line 1: `V E` (V vertices, E edges)
- Lines 2+: `u v weight` (edge from u to v with weight)

**Example file:** `data/sample_input.txt`

### Output Format

#### Single-Source (Dijkstra, Bellman-Ford)
```
Shortest Paths from Source 1:
Vertex     Distance
------     --------
1          0
2          2
3          3
4          9
5          6
```

#### All-Pairs (Floyd-Warshall, Johnson)
```
Distance Matrix (5x5):
     1       2       3       4       5
1:   0       2       3       9       6
2:   INF     0       1       7       4
3:   INF     INF     0       INF     3
4:   INF     INF     INF     0       1
5:   INF     2       INF     2       0
```

---

## Sample Data Files

### Available Test Graphs

1. **data/sample_input.txt**
   - 5 vertices, 7 edges
   - Positive weights only
   - Basic example from project spec

2. **data/test_graphs/negative_weights.txt**
   - 4 vertices, 4 edges
   - Contains negative weights (no cycle)
   - Tests Bellman-Ford, Floyd-Warshall, Johnson

3. **data/test_graphs/sparse_10v.txt**
   - 10 vertices, 15 edges
   - Sparse graph (E ≈ V)
   - Tests algorithm scalability

### Built-in Sample Graphs (in memory)

When running the interactive menu, you can test on 3 built-in graphs:

1. **sample** - Basic 5-vertex graph
2. **disconnected** - Tests handling of unreachable vertices
3. **negative_weights** - Tests handling of negative edges

---

## Understanding the Output

### Dijkstra & Bellman-Ford Output

Shows shortest distance from source to each vertex:
- Source vertex always has distance 0
- INF means vertex is unreachable
- Negative distances indicate negative weights

Example:
```
Vertex 1 Distance: 0   (source)
Vertex 2 Distance: 2   (1→2 costs 2)
Vertex 3 Distance: 3   (1→3 costs 4, but 1→2→3 costs 3)
```

### Floyd-Warshall & Johnson Output

Shows distance matrix for ALL pairs:
- Diagonal is 0 (distance from vertex to itself)
- dist[i][j] = shortest distance from i to j
- INF = no path exists

Example:
```
dist[1][3] = 3   means shortest path from 1 to 3 is 3
dist[2][1] = INF means no path exists from 2 to 1
```

### Benchmark Metrics

- **Execution Time**: How long algorithm took (in seconds)
- **Relaxations**: Number of edge relaxations performed
- **Memory Usage**: Peak memory used (in KB)

Lower is better for all metrics.

---

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'src'"

**Solution:** Make sure you're running from the project root directory:
```bash
cd C:\Users\admin\Documents\AlgoAssignments\graph-routing-algos
python -m src.main
```

### Error: "FileNotFoundError: data/xxx.txt"

**Solution:** Ensure you're in the project root and the file exists in `data/` folder.

### Error: "No module named 'pytest'"

**Solution:** Install pytest if you want to run tests:
```bash
pip install pytest
```

Or use unittest instead:
```bash
python -m unittest tests.test_dijkstra
```

### Algorithm takes too long

**Solution:** You're probably running Floyd-Warshall or Johnson on a large dense graph. These have O(V³) and O(V²logV) complexity. Try with smaller graphs first.

---

## Testing Algorithms

### Run All Tests
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Run Specific Algorithm Tests
```bash
python -m unittest tests.test_dijkstra -v
python -m unittest tests.test_bellman_ford -v
python -m unittest tests.test_floyd_warshall -v
python -m unittest tests.test_johnson -v
```

### Expected Test Results
- **test_dijkstra.py**: 7 tests
- **test_bellman_ford.py**: 8 tests
- **test_floyd_warshall.py**: 9 tests
- **test_johnson.py**: 9 tests

Total: 33 unit tests

---

## Analyzing Results

### Comparing Algorithm Performance

Run option 3 or 4 from main menu to see:

1. **Execution Time Comparison**
   - Dijkstra: Fastest for non-negative, sparse
   - Bellman-Ford: Slower, handles negatives
   - Floyd-Warshall: O(V³), good for small dense
   - Johnson: Best for sparse all-pairs

2. **Relaxation Count**
   - Indicates algorithm iterations
   - Lower = more efficient

3. **Memory Usage**
   - Single-source: O(V)
   - All-pairs: O(V²)

### When to Use Each

**Dijkstra** → Fastest for non-negative weights
**Bellman-Ford** → When negative weights present (single-source)
**Floyd-Warshall** → All-pairs, small graphs (V < 500)
**Johnson** → All-pairs, sparse graphs

---

## Generating Custom Test Graphs

Edit `src/analysis/graph_generator.py` to create custom graphs:

```python
from src.analysis.graph_generator import generate_sparse_graph, generate_dense_graph

# Generate sparse graph with 20 vertices
sparse = generate_sparse_graph(20)

# Generate dense graph with 15 vertices
dense = generate_dense_graph(15)

# Generate mixed graph with negative weights
mixed = generate_mixed_graph(25, include_negatives=True)
```

---

## Documentation

- **algorithm_explanations.md**: Detailed info on each algorithm
- **report.md**: Main project report
- **experimental_results.md**: Generated after running full suite
- **project.md**: Original project specification

---

## Contact & Support

For issues or questions:
1. Check the troubleshooting section above
2. Review algorithm_explanations.md for algorithm details
3. Check test files for usage examples
4. Review graph_utils.py for Graph class documentation

---

## Quick Reference Commands

```bash
# Start interactive menu
python -m src.main

# Run all tests
python -m unittest discover -s tests

# Run specific test
python -m unittest tests.test_dijkstra -v

# Generate full comparison report
python -c "from src.analysis.compare_algorithms import run_full_comparison; run_full_comparison()"

# View available graphs
python -c "from src.graph_utils import create_sample_graphs; [g.print_graph() for g in create_sample_graphs().values()]"
```
