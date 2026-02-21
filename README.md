# PageRank Simulator

A browser-based interactive simulator for the PageRank algorithm. Build custom graphs, configure algorithm parameters, and observe convergence iteration by iteration.

## Features

- Add/remove nodes and directed edges with a point-and-click interface
- Toggle **with damping** (standard) or **no damping** (d=1) mode
- Toggle **dangling node handling** on/off to compare rank leakage vs. correct redistribution
- Configurable damping factor (d), tolerance, and max iterations
- Live graph canvas — drag nodes, zoom, pan
- Node size scales with PageRank value post-computation
- Iteration slider to replay any step of the algorithm
- Convergence curve chart and full iteration log table
- 5 preloaded sample graphs (tutorial, web graph, cycle, star, multi-sink)

## Algorithm

Standard iterative PageRank:

PR(i) = (1 - d) / N + d × Σ [ PR(j) / L(j) ]

With dangling node correction at each iteration:

PR(i) += d × (Σ PR(dangling) / N)

Converges when the total absolute difference between iterations falls below the set tolerance.

## Usage

No installation or dependencies. Open `pagerank_simulator.html` directly in any modern browser.

page_rank_damping.py is the CLI based implimentation of this algorithm in the CLI based.

## Parameters

| Parameter         | Default | Description                                       |
| ----------------- | ------- | ------------------------------------------------- |
| Damping (d)       | 0.85    | Probability of following a link vs. teleporting   |
| Tolerance         | 1e-6    | Convergence threshold (sum of absolute Δ)        |
| Max Iterations    | 100     | Hard stop if convergence not reached              |
| Dangling Handling | ON      | Redistributes rank from sink nodes each iteration |

More updates to come!
