import sys
import os
from src.graph_utils import Graph, read_graph_from_file, create_sample_graphs, write_graph_to_file
from src.algorithms.dijkstra import dijkstra, print_distances as dijkstra_print
from src.algorithms.bellman_ford import bellman_ford, print_distances as bellman_ford_print
from src.algorithms.floyd_warshall import floyd_warshall, print_specific_distances as fw_print
from src.algorithms.johnson import johnson, print_specific_distances as johnson_print
from src.analysis.benchmark import benchmark_all, create_comparison_table
from src.analysis.compare_algorithms import run_full_comparison


def print_menu():
    print("\n" + "="*60)
    print("SHORTEST PATH ALGORITHMS - ANALYSIS SYSTEM")
    print("="*60)
    print("\n1. Load graph from file")
    print("2. Run specific algorithm on sample graph")
    print("3. Compare all algorithms on sample graphs")
    print("4. Run full comparison suite (sparse/dense/mixed)")
    print("5. Benchmark single algorithm")
    print("6. View sample graphs")
    print("7. Exit")
    print("\nSelect option (1-7): ", end="")


def load_and_process_graph():
    filename = input("Enter graph filename (in data/ folder): ").strip()
    filepath = os.path.join("data", filename)
    
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return None
    
    graph = read_graph_from_file(filepath)
    if graph is None:
        return None
    
    print(f"\nGraph loaded successfully!")
    print(f"Vertices: {graph.num_vertices}")
    print(f"Edges: {len(graph.edges)}")
    
    if graph.has_negative_cycle():
        print(" WARNING: Graph contains negative cycles!")
    
    graph.print_graph()
    return graph


def run_single_algorithm():
    samples = create_sample_graphs()
    
    print("\nAvailable sample graphs:")
    for i, (name, _) in enumerate(samples.items(), 1):
        print(f"  {i}. {name}")
    
    choice = input("Select graph (1-3): ").strip()
    graph_name = list(samples.keys())[int(choice) - 1] if choice.isdigit() else None
    
    if graph_name is None:
        print("Invalid choice")
        return
    
    graph = samples[graph_name]
    print(f"\n### Processing {graph_name} graph ###")
    graph.print_graph()
    
    print("\nSelect algorithm:")
    print("1. Dijkstra (single-source, non-negative)")
    print("2. Bellman-Ford (single-source, handles negatives)")
    print("3. Floyd-Warshall (all-pairs)")
    print("4. Johnson (all-pairs, efficient)")
    
    algo_choice = input("Select algorithm (1-4): ").strip()
    
    source = 1
    if algo_choice in ['1', '2']:
        source = int(input(f"Enter source vertex (1-{graph.num_vertices}): ") or "1")
    
    if algo_choice == '1':
        distances, relaxations = dijkstra(graph, source)
        dijkstra_print(distances, source)
        print(f"Relaxations: {relaxations}")
    
    elif algo_choice == '2':
        distances, relaxations, has_cycle = bellman_ford(graph, source)
        bellman_ford_print(distances, source, has_cycle)
        print(f"Relaxations: {relaxations}")
    
    elif algo_choice == '3':
        dist_matrix, relaxations, has_cycle = floyd_warshall(graph)
        if not has_cycle:
            fw_print(dist_matrix, source, graph.num_vertices)
            print(f"Relaxations: {relaxations}")
        else:
            print(" Negative cycle detected!")
    
    elif algo_choice == '4':
        dist_matrix, relaxations, has_cycle = johnson(graph)
        if not has_cycle and dist_matrix is not None:
            johnson_print(dist_matrix, source, graph.num_vertices)
            print(f"Relaxations: {relaxations}")
        else:
            print(" Negative cycle detected or algorithm failed!")


def compare_sample_graphs():
    samples = create_sample_graphs()
    results = {}
    
    print("\n" + "="*60)
    print("COMPARING ALL ALGORITHMS ON SAMPLE GRAPHS")
    print("="*60)
    
    for name, graph in samples.items():
        print(f"\n### {name.upper()} ###")
        graph.print_graph()
        results[name] = benchmark_all(graph, f"Sample_{name}", source=1)
    
    # Print comparison table
    create_comparison_table(results)


def run_full_suite():
    print("\n" + "="*60)
    print("RUNNING FULL COMPARISON SUITE")
    print("This may take a few minutes...")
    print("="*60)
    
    mode = input("Select mode: [q]uick (default) or [l]arge (adds 100/200 dense)? ").strip().lower()
    mode = "large" if mode in ["l", "large"] else "quick"
    
    comparison = run_full_comparison(mode=mode)
    comparison.save_report("results/result.txt")


def benchmark_single():
    samples = create_sample_graphs()
    
    print("\nAvailable sample graphs:")
    for i, (name, _) in enumerate(samples.items(), 1):
        print(f"  {i}. {name}")
    
    choice = input("Select graph (1-3): ").strip()
    graph_name = list(samples.keys())[int(choice) - 1] if choice.isdigit() else None
    
    if graph_name is None:
        print("Invalid choice")
        return
    
    graph = samples[graph_name]
    
    print("\nSelect algorithm:")
    print("1. Dijkstra")
    print("2. Bellman-Ford")
    print("3. Floyd-Warshall")
    print("4. Johnson")
    
    algo_choice = input("Select algorithm (1-4): ").strip()
    
    from src.analysis.benchmark import (
        benchmark_dijkstra, benchmark_bellman_ford,
        benchmark_floyd_warshall, benchmark_johnson
    )
    
    if algo_choice == '1':
        result = benchmark_dijkstra(graph, source=1)
        print(result)
    elif algo_choice == '2':
        result = benchmark_bellman_ford(graph, source=1)
        print(result)
    elif algo_choice == '3':
        result = benchmark_floyd_warshall(graph)
        print(result)
    elif algo_choice == '4':
        result = benchmark_johnson(graph)
        print(result)
    else:
        print("Invalid choice")


def view_samples():
    samples = create_sample_graphs()
    
    print("\n" + "="*60)
    print("SAMPLE GRAPHS")
    print("="*60)
    
    for name, graph in samples.items():
        print(f"\n### {name.upper()} ###")
        print(f"Vertices: {graph.num_vertices}, Edges: {len(graph.edges)}")
        graph.print_graph()
        graph.print_matrix()


def main():
    while True:
        print_menu()
        choice = input().strip()
        
        try:
            if choice == '1':
                graph = load_and_process_graph()
                if graph:
                    print("\nWhat would you like to do?")
                    print("1. Run Dijkstra")
                    print("2. Run Bellman-Ford")
                    print("3. Run Floyd-Warshall")
                    print("4. Run Johnson")
                    algo_choice = input("Choice (1-4): ").strip()
                    
                    source = 1
                    if algo_choice in ['1', '2']:
                        source = int(input("Enter source vertex: ") or "1")
                    
                    if algo_choice == '1':
                        distances, _ = dijkstra(graph, source)
                        dijkstra_print(distances, source)
                    elif algo_choice == '2':
                        distances, _, has_cycle = bellman_ford(graph, source)
                        bellman_ford_print(distances, source, has_cycle)
                    elif algo_choice == '3':
                        dist, _, has_cycle = floyd_warshall(graph)
                        if not has_cycle:
                            fw_print(dist, source, graph.num_vertices)
                    elif algo_choice == '4':
                        dist, _, has_cycle = johnson(graph)
                        if not has_cycle and dist is not None:
                            johnson_print(dist, source, graph.num_vertices)
            
            elif choice == '2':
                run_single_algorithm()
            
            elif choice == '3':
                compare_sample_graphs()
            
            elif choice == '4':
                run_full_suite()
            
            elif choice == '5':
                benchmark_single()
            
            elif choice == '6':
                view_samples()
            
            elif choice == '7':
                print("\nThank you for using the Shortest Path Analysis System!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted.")
            break
        except Exception as e:
            print(f"\nError: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
