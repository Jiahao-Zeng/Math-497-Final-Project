---
layout: article
title: Phase 1
permalink: /phase1/
use_math: true
---

## Overview

This project numerically solves the linear advection equation using a finite difference upwind scheme. The main goal is to simulate how a constant-density wave propagates over time and space, compare it with the exact analytical solution, and analyze the error behavior as we refine the spatial grid.

## Implementation Details

- Domain: $0 \le x \le 1$, $0 \le t \le 2$
- Uniform grids in both time and space
- Time step $\Delta t$ is chosen based on the CFL condition:

$$
\Delta t = 0.8 \cdot \Delta x
$$

- Initial condition:

$$
\rho(x, 0) = 0
$$

- Boundary condition:

$$
\rho(0, t) = \rho_L
$$

- **Numerical scheme (Upwind method):**

$$
P_j^{n+1} = (1 - v) \cdot P_j^n + v \cdot P_{j-1}^n
$$

- The numerical solution is compared with exact solutions at:
  - A fixed **spatial point** $x = 0.5$ over time
  - A fixed **time** $t = 0.5$ across space

- **Error is computed** using the L1 norm:

$$
\text{Error} = \Delta x \sum_j \left| \rho_{\text{exact}} - \rho_{\text{numerical}} \right|
$$


## Key Components
- $dx$, $dt$ grid sizing controlled by CFL condition
- Time-stepping loop with nested space updates
- **Boundary condition** applied at the leftmost column of $P$
- **Exact solution arrays** used for validation
- **Error analysis** across multiple $\Delta x$ values and time levels
- Visualizations:
  - Numerical vs exact plots at fixed $x$ or $t$
  - Log-log plots of error vs $\Delta x$
  - 3D surface plot of solution over $x$ and $t$

## Results and Analysis

- Numerical solutions converge to the exact solution as $\Delta x \to 0$
- Error **decreases steadily**, confirming **first-order accuracy**
- Upwind scheme is **stable**, but exhibits **diffusive behavior** near discontinuities
- 3D surface visualization confirms correct wave speed and evolution
- Behavior aligns with theoretical expectations for first-order advection solvers


## Next Steps

- Implement **higher-order schemes** (e.g., Lax-Wendroff, ENO, WENO) for sharper wave fronts
- Add **adaptive mesh refinement (AMR)** to improve resolution where needed
- Extend to **nonlinear PDEs** like Burgers’ equation or systems with shocks
- Introduce **discontinuous initial or boundary conditions**
- Create **animations** of wave propagation for improved visualization

[Continue to Phase 2 →]({{ '/phase2' | relative_url }}) 
