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

---

### 1. Compare Filtered vs Upwind Across Multiple $\Delta x$ and $\gamma$

- Build on Phase 2's filtered scheme evaluation by **quantifying convergence** more formally:
  - Vary $\Delta x$ from $2^{-4}$ to $2^{-8}$
  - Compare performance for $\gamma = 0$ (upwind) and $\gamma = 1.75$ (filtered)
- Use consistent time $t = 0.4$ to compute error and plot:
  $$
  \log(\text{Error}) \text{ vs } \log(\Delta x)
  $$
- Confirm whether **first-order convergence** is maintained under different $\gamma$ values.

---

### 2. Evaluate Temporal Profiles at Fixed Location

- Extend the temporal comparison at $x = 0.5$ by overlaying:
  - Upwind scheme
  - Filtered scheme with multiple $\gamma$ values
  - Exact solution
- Analyze how different filters affect:
  - Arrival time accuracy
  - Transition sharpness
  - Oscillatory behavior

---

### 3. Cross-Sectional Accuracy at Fixed Time

- Fix $t = 0.4$ and examine $\rho(x, t)$ across the full domain:
  - Highlight regions where filtering smooths or sharpens the wavefront
  - Visually inspect **shock width** and **location of the front**

---

### 4. Introduce Periodic Initial and Boundary Conditions

- Use sinusoidal data:
  $$
  \rho(x, 0) = \sin(2\pi x), \quad \rho(0,t) = \rho(1,t)
  $$
- Simulate for long durations ($t = 2T,\ 5T,\ 10T$)
- Evaluate how well each scheme preserves the periodic structure over time:
  - Identify **phase errors**
  - Compare wave amplitude and shape retention

---

### 5. Vectorize the Scheme for Efficiency

- Rewrite time-stepping with **NumPy operations**:
  - Use `np.roll` to shift values for periodic BCs
  - Replace inner loops with vectorized expressions
- This will allow simulation for **longer times** and **finer grids** without performance loss

---

### 6. Prepare Visual Assets

- Create standardized plots for:
  - Solution snapshots
  - Error convergence
  - Wave propagation
- Generate animations for the periodic problem to visualize continuous wave motion under different $\gamma$ values

---


[Continue to Phase 3 →]({{ '/phase3' | relative_url }}) 
