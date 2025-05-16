---
layout: article
title: Phase 2
permalink: /phase2/
use_math: true
---

## Overview

This phase explores the behavior of a **filtered upwind scheme** for the linear advection equation. The filter parameter $\gamma$ controls the balance between numerical diffusion and accuracy. Two test cases are studied:

- Case A: $\rho_L = 0.5$, $\gamma = 1.75$
- Case B: $\rho_L = 0.25$, $\gamma = 0.75$

The goal is to assess solution accuracy, compare with the exact profile, and measure the convergence rate as $\Delta x$ decreases.

---


## Implementation Details

- The numerical method builds on the **upwind scheme** and introduces a **filtering mechanism** controlled by $\gamma$.
- The PDE being solved is:

$$
\rho_t + v \rho_x = 0, \quad \text{with constant } v
$$

- Time discretization uses:

$$
\Delta t = 0.8 \cdot \Delta x \cdot \left( \frac{2 - \gamma}{2 + \gamma} \right)
$$

- The **Courant number** is:

$$
\nu = \frac{v \Delta t}{\Delta x}
$$

- The first time step uses the basic upwind scheme:

$$
P_j^1 = (1 - \nu) P_j^0 + \nu P_{j-1}^0
$$

- Subsequent time steps follow the filtered scheme:

$$
P_j^{n+1} =
\left( \gamma + (1 - \nu) \left(1 - \frac{\gamma}{2} \right) \right) P_j^n
- \frac{\gamma}{2} P_j^{n-1}
+ \nu \left( 1 - \frac{\gamma}{2} \right) P_{j-1}^n
$$

- Two types of comparisons are made:
  1. **Fixed spatial point** $x = 0.5$, plot $\rho(t)$
  2. **Fixed time** $t = 0.5$, plot $\rho(x)$

---

## Key Improvements

- **Filtered Upwind Scheme** with adjustable $\gamma$
- **Initial and boundary conditions:**
  - $\rho(x,0) = 0$
  - $\rho(0,t) = \rho_L$
- **Exact solution:**
  - At position $x = 0.5$: $\rho = \rho_L$ if $v t > 0.5$, else $0$
  - At time $t = 0.5$: $\rho = \rho_L$ if $x < v t$, else $0$
- **Error calculation:** L1-norm across spatial domain

$$
\text{Error} = \Delta x \sum_j \left| \rho_{\text{exact}} - \rho_{\text{numerical}} \right|
$$

- **Error table:** computed for multiple values of $\Delta x$ at fixed time snapshots $t = 0.2, 0.4, 0.6, 0.8, 1.0$
- **Log-log error plots** to visualize convergence behavior

---

## Results and Analysis
### Case A: $\rho_L = 0.5$, $\gamma = 1.75$
- The filtered scheme produced smoother profiles than upwind and more accurate representation near the discontinuity.
- The solution at $x = 0.5$ matches the exact value after $t > 1$.
- At $t = 0.5$, the scheme preserves the wavefront with some diffusion, especially for coarser $\Delta x$.

### Case B: $\rho_L = 0.25$, $\gamma = 0.75$
- Less aggressive filtering leads to reduced smoothing and sharper wavefronts.
- Error at early times ($t = 0.2$) is higher, but long-time behavior improves.
- This shows the filtered scheme is sensitive to $\gamma$ and initial conditions.

### Error Convergence
- In both cases, the error decreases as $\Delta x$ decreases.
- The **log-log plots of error vs $\Delta x$** show near-linear decay, indicating consistent convergence.
- The rate of convergence is dependent on $\gamma$, with moderate values (like $\gamma = 0.75$) performing better in preserving sharp transitions.

### Surface Plot
- The 3D plot of $\rho(x,t)$ shows clear rightward wave propagation.
- Smoother transitions occur as $\gamma$ increases.
- The surface remains stable and consistent with expectations for hyperbolic PDEs.

---


## Next Steps

Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.

[Continue to Phase 3 →]({{ '/phase3' | relative_url }}) 
