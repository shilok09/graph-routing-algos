from typing import Dict, List
from src.analysis.graph_generator import (
    generate_sparse_graph,
    generate_dense_graph,
    generate_mixed_graph,
    generate_complete_graph
)
from src.analysis.benchmark import benchmark_all, create_comparison_table
from src.graph_utils import Graph


class AlgorithmComparison:
    """Compare shortest path algorithms."""
    
    def __init__(self):
        self.results = {}
        self.summary = {}
    
    def compare_sparse_graphs(self) -> None:
        """Compare algorithms on sparse graphs."""
        print("\n" + "="*80)
        print("COMPARING SPARSE GRAPHS")
        print("="*80)
        
        for num_vertices in [10, 25, 50]:
            graph = generate_sparse_graph(num_vertices)
            test_name = f"Sparse_{num_vertices}V"
            results = benchmark_all(graph, test_name, source=1)
            self.results[test_name] = results
    
    def compare_dense_graphs(self) -> None:
        """Compare algorithms on dense graphs."""
        print("\n" + "="*80)
        print("COMPARING DENSE GRAPHS")
        print("="*80)
        
        for num_vertices in [10, 25, 50]:
            graph = generate_dense_graph(num_vertices)
            test_name = f"Dense_{num_vertices}V"
            results = benchmark_all(graph, test_name, source=1)
            self.results[test_name] = results
    
    def compare_mixed_graphs(self) -> None:
        """Compare algorithms on mixed graphs with negative weights."""
        print("\n" + "="*80)
        print("COMPARING MIXED GRAPHS (with negative weights)")
        print("="*80)
        
        for num_vertices in [10, 25, 50]:
            graph = generate_mixed_graph(num_vertices, include_negatives=True)
            test_name = f"Mixed_{num_vertices}V"
            results = benchmark_all(graph, test_name, source=1)
            self.results[test_name] = results
    
    def generate_analysis_report(self) -> str:
        report = "\n" + "="*80 + "\n"
        report += "ALGORITHM COMPARISON ANALYSIS\n"
        report += "="*80 + "\n"
        
        report += "\n### BEST ALGORITHMS BY GRAPH TYPE ###\n"
        
        # Group by graph type
        graph_types = {}
        for test_name, results in self.results.items():
            graph_type = test_name.rsplit('_', 1)[0]
            if graph_type not in graph_types:
                graph_types[graph_type] = {}
            graph_types[graph_type][test_name] = results
        
        for graph_type, tests in sorted(graph_types.items()):
            report += f"\n{graph_type.upper()}:\n"
            report += "-" * 40 + "\n"
            
            # Find fastest algorithm overall for this type
            all_times = {}
            for test_name, results in tests.items():
                for algo_name, result in results.items():
                    if result.success:
                        if algo_name not in all_times:
                            all_times[algo_name] = 0
                        all_times[algo_name] += result.execution_time
            
            if all_times:
                fastest = min(all_times, key=all_times.get)
                report += f"Fastest Algorithm: {fastest}\n"
                report += f"Average Time: {all_times[fastest]/len(tests):.6f}s\n"
            
            # Show breakdown by size
            for test_name in sorted(tests.keys()):
                report += f"\n  {test_name}:\n"
                for algo_name, result in sorted(tests[test_name].items()):
                    if result.success:
                        report += f"    {algo_name}: {result.execution_time:.6f}s, Relaxations: {result.relaxations}\n"
                    else:
                        report += f"    {algo_name}: FAILED - {result.error_message}\n"
        
        report += "\n### ALGORITHM CHARACTERISTICS ###\n"
        report += "-" * 40 + "\n"
        report += "Dijkstra:\n"
        report += "  - Best for: Non-negative weights, single-source\n"
        report += "  - Time: O((V+E)log V) with heap\n"
        report += "  - Space: O(V)\n\n"
        
        report += "Bellman-Ford:\n"
        report += "  - Best for: Negative weights, single-source\n"
        report += "  - Time: O(VE)\n"
        report += "  - Can detect negative cycles\n\n"
        
        report += "Floyd-Warshall:\n"
        report += "  - Best for: All-pairs, small dense graphs\n"
        report += "  - Time: O(V^3)\n"
        report += "  - Space: O(V^2)\n\n"
        
        report += "Johnson:\n"
        report += "  - Best for: All-pairs sparse graphs\n"
        report += "  - Time: O(V^2 log V + VE)\n"
        report += "  - Better than Floyd-Warshall for sparse\n"
        
        return report
    
    def save_report(self, filename: str) -> None:
        report = self.generate_analysis_report()
        with open(filename, 'w') as f:
            f.write(report)
        print(f"Report saved to {filename}")
    
    def print_summary(self) -> None:
        """Print summary of comparisons."""
        print("\n" + "="*80)
        print("SUMMARY")
        print("="*80)
        print(self.generate_analysis_report())


def run_full_comparison(mode: str = "quick") -> None:
    comparison = AlgorithmComparison()
    
    # Run all comparisons (quick set)
    comparison.compare_sparse_graphs()
    comparison.compare_dense_graphs()
    comparison.compare_mixed_graphs()
    
    # Optionally add large dense graphs
    if mode == "large":
        print("\n" + "="*80)
        print("COMPARING LARGE DENSE GRAPHS (100, 200 vertices) - this may take long")
        print("="*80)
        for num_vertices in [100, 200]:
            from src.analysis.graph_generator import generate_dense_graph
            graph = generate_dense_graph(num_vertices)
            test_name = f"Dense_{num_vertices}V_Large"
            results = benchmark_all(graph, test_name, source=1)
            comparison.results[test_name] = results
    
    comparison.print_summary()
    create_comparison_table(comparison.results)
    
    return comparison


if __name__ == "__main__":
    run_full_comparison()
