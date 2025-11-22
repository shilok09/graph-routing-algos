import time
import tracemalloc
from typing import Callable, Dict, Tuple, Any
from src.graph_utils import Graph
from src.algorithms.dijkstra import dijkstra
from src.algorithms.bellman_ford import bellman_ford
from src.algorithms.floyd_warshall import floyd_warshall
from src.algorithms.johnson import johnson


class BenchmarkResult:
    """Store benchmark results for an algorithm."""
    
    def __init__(self, algorithm_name: str):
        self.algorithm_name = algorithm_name
        self.execution_time = 0.0
        self.relaxations = 0
        self.memory_usage = 0
        self.success = False
        self.error_message = None
    
    def __str__(self):
        result = f"\n{self.algorithm_name}:\n"
        result += f"  Execution Time: {self.execution_time:.6f} seconds\n"
        result += f"  Relaxations: {self.relaxations}\n"
        result += f"  Memory Usage: {self.memory_usage:.2f} KB\n"
        result += f"  Success: {self.success}\n"
        if self.error_message:
            result += f"  Error: {self.error_message}\n"
        return result


def benchmark_dijkstra(graph: Graph, source: int = 1) -> BenchmarkResult:
    """Benchmark Dijkstra's algorithm."""
    result = BenchmarkResult("Dijkstra's Algorithm")
    
    try:
        tracemalloc.start()
        start_time = time.perf_counter()
        
        distances, relaxations = dijkstra(graph, source)
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        result.execution_time = end_time - start_time
        result.relaxations = relaxations
        result.memory_usage = peak / 1024  # Convert to KB
        result.success = True
        
    except Exception as e:
        result.error_message = str(e)
        result.success = False
    
    return result


def benchmark_bellman_ford(graph: Graph, source: int = 1) -> BenchmarkResult:
    """Benchmark Bellman-Ford algorithm."""
    result = BenchmarkResult("Bellman-Ford Algorithm")
    
    try:
        tracemalloc.start()
        start_time = time.perf_counter()
        
        distances, relaxations, has_negative_cycle = bellman_ford(graph, source)
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        result.execution_time = end_time - start_time
        result.relaxations = relaxations
        result.memory_usage = peak / 1024  # Convert to KB
        result.success = not has_negative_cycle
        
        if has_negative_cycle:
            result.error_message = "Negative cycle detected"
        
    except Exception as e:
        result.error_message = str(e)
        result.success = False
    
    return result


def benchmark_floyd_warshall(graph: Graph) -> BenchmarkResult:
    """Benchmark Floyd-Warshall algorithm."""
    result = BenchmarkResult("Floyd-Warshall Algorithm")
    
    try:
        tracemalloc.start()
        start_time = time.perf_counter()
        
        dist_matrix, relaxations, has_negative_cycle = floyd_warshall(graph)
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        result.execution_time = end_time - start_time
        result.relaxations = relaxations
        result.memory_usage = peak / 1024  # Convert to KB
        result.success = not has_negative_cycle
        
        if has_negative_cycle:
            result.error_message = "Negative cycle detected"
        
    except Exception as e:
        result.error_message = str(e)
        result.success = False
    
    return result


def benchmark_johnson(graph: Graph) -> BenchmarkResult:
    """Benchmark Johnson's algorithm."""
    result = BenchmarkResult("Johnson's Algorithm")
    
    try:
        tracemalloc.start()
        start_time = time.perf_counter()
        
        dist_matrix, relaxations, has_negative_cycle = johnson(graph)
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        result.execution_time = end_time - start_time
        result.relaxations = relaxations
        result.memory_usage = peak / 1024  # Convert to KB
        result.success = not has_negative_cycle
        
        if has_negative_cycle:
            result.error_message = "Negative cycle detected"
        
    except Exception as e:
        result.error_message = str(e)
        result.success = False
    
    return result


def benchmark_all(graph: Graph, test_name: str = "Test", source: int = 1) -> Dict[str, BenchmarkResult]:
    """
    Benchmark all algorithms on a graph.
    
    Args:
        graph: Graph to test
        test_name: Name of the test
        source: Source vertex for single-source algorithms
        
    Returns:
        Dictionary of algorithm names to benchmark results
    """
    print(f"\n{'='*60}")
    print(f"Benchmarking on: {test_name}")
    print(f"Graph: {graph.num_vertices} vertices, {len(graph.edges)} edges")
    print(f"{'='*60}")
    
    results = {}
    
    # Single-source algorithms
    print("\nRunning Dijkstra's Algorithm...")
    results['dijkstra'] = benchmark_dijkstra(graph, source)
    
    print("Running Bellman-Ford Algorithm...")
    results['bellman_ford'] = benchmark_bellman_ford(graph, source)
    
    # All-pairs algorithms
    print("Running Floyd-Warshall Algorithm...")
    results['floyd_warshall'] = benchmark_floyd_warshall(graph)
    
    print("Running Johnson's Algorithm...")
    results['johnson'] = benchmark_johnson(graph)
    
    # Print results
    for name, result in results.items():
        print(result)
    
    return results


def create_comparison_table(results_dict: Dict[str, Dict[str, BenchmarkResult]]) -> None:
    """
    Create a comparison table from multiple benchmark runs.
    
    Args:
        results_dict: Dictionary mapping test names to benchmark results
    """
    print(f"\n{'='*100}")
    print("BENCHMARK COMPARISON TABLE")
    print(f"{'='*100}\n")
    
    # Create header
    print(f"{'Test Name':<20} {'Algorithm':<20} {'Time (s)':<15} {'Relaxations':<15} {'Memory (KB)':<15}")
    print("-" * 100)
    
    for test_name, results in sorted(results_dict.items()):
        for algo_name, result in sorted(results.items()):
            if result.success:
                print(f"{test_name:<20} {result.algorithm_name:<20} {result.execution_time:<15.6f} {result.relaxations:<15} {result.memory_usage:<15.2f}")
            else:
                print(f"{test_name:<20} {result.algorithm_name:<20} {'FAILED':<15} {result.error_message:<15}")
