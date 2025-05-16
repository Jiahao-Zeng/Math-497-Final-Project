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

##Next Steps

Based on the current implementation comparing the **filtered upwind scheme** to the **basic upwind method**, here are focused directions for future development:

---

###  **1. Explore the effect of $\gamma$**

- Systematically vary $\gamma$ (e.g., $0$, $0.5$, $1$, $1.75$, $2$) and observe how it influences:
  - **Numerical diffusion**
  - **Accuracy near discontinuities**
  - **Stability** and **smoothness** of the solution
- Plot solution profiles and error curves for each $\gamma$ to identify optimal values for different scenarios.

---

###  **2. Compare with basic upwind scheme**

- Run both schemes under identical conditions and compare:
  - **Pointwise error** over time and space
  - **Convergence behavior** as $\Delta x \to 0$
  - **Stability behavior** at coarser resolutions
- Highlight the advantages of filtering in reducing artificial smearing or oscillation.

---

###  **3. Theoretical analysis**

- Use Taylor series expansion to analyze the **local truncation error** of both schemes.
- Confirm that the filtered scheme achieves improved accuracy as intended when $\gamma$ is chosen appropriately.
- Assess how the error changes in space vs. time.

---

###  **4. Boundary and initial condition testing**

- Test with non-standard conditions:
  - Discontinuous initial condition
  - Time-dependent boundary value
- Observe whether the filtered scheme handles **sharp transitions** better than the basic upwind method.

---

### � **5. Enhance visualization and diagnostics**

- Animate solution over time to visualize the propagation behavior of each scheme.
- Use color-coded surface plots for direct comparison.
- Add diagnostics like:
  - $\max$ and $\min$ values at each time step
  - Total variation to measure oscillation

---

###  **6. Automate error analysis**

- Automatically compute and format:
  - **Error tables** across $\gamma$ and $\Delta x$
  - **Log-log plots** showing convergence rates
- Output results for reports or presentations.


[Continue to Phase 2 →]({{ '/phase2' | relative_url }}) 
