def pagerank_with_dangling(graph, d=0.85, tol=1e-6, max_iter=100):
    nodes = list(graph.keys())
    N = len(nodes)
    
    # Initial PR
    PR = {node: 1/N for node in nodes}
    
    # Find dangling nodes (no outlinks)
    dangling_nodes = [node for node in nodes if not graph[node]]
    
    print(f"Nodes: {nodes}")
    print(f"N = {N}, d = {d}")
    print(f"Dangling nodes: {dangling_nodes}")
    print(f"\n{'='*60}")
    print(f"Iteration 0 (Initial):")
    for node in nodes:
        print(f"  PR({node}) = {PR[node]:.4f}")
    print(f"  Sum = {sum(PR.values()):.4f}")
    
    for iteration in range(1, max_iter + 1):
        # Step 1: Collect dangling node rank
        dangling_sum = sum(PR[node] for node in dangling_nodes)
        dangling_contribution = d * (dangling_sum / N)
        
        new_PR = {}
        for node in nodes:
            # Base teleportation
            rank = (1 - d) / N
            
            # Dangling node redistribution
            rank += dangling_contribution
            
            # Normal inlink contributions
            for src in nodes:
                if node in graph[src]:  # src links to node
                    rank += d * (PR[src] / len(graph[src]))
            
            new_PR[node] = rank
        
        print(f"\nIteration {iteration}:")
        print(f"  Dangling sum = {dangling_sum:.6f}, Contribution to each = {dangling_contribution:.6f}")
        for node in nodes:
            print(f"  PR({node}) = {new_PR[node]:.4f}  (was {PR[node]:.4f})")
        print(f"  Sum = {sum(new_PR.values()):.4f}")
        
        # Check convergence
        diff = sum(abs(new_PR[node] - PR[node]) for node in nodes)
        print(f"  Total diff = {diff:.8f}")
        
        PR = new_PR
        
        if diff < tol:
            print(f"\n{'='*60}")
            print(f"CONVERGED at iteration {iteration} (diff={diff:.2e} < tol={tol})")
            break
    else:
        print(f"\n{'='*60}")
        print(f"Did not converge within {max_iter} iterations")
    
    print(f"\nFinal PageRank:")
    for node in sorted(PR.keys()):
        print(f"  PR({node}) = {PR[node]:.6f}")
    print(f"  Total sum = {sum(PR.values()):.6f}")
    
    return PR


# Your graph
graph = {
    'p1': ['p2', 'p5', 'p4'],
    'p2': [],           # dangling node
    'p3': ['p1', 'p4'],
    'p4': ['p3'],
    'p5': ['p1', 'p3']
}

final_PR = pagerank_with_dangling(graph, d=0.85, tol=1e-6)