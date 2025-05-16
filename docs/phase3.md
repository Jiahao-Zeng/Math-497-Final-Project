---
layout: article
title: Phase 3
permalink: /phase3/
use_math: true
---

## Overview

This phase extends the evaluation of the filtered upwind scheme by:

- Performing a **side-by-side error analysis** between $\gamma = 0$ (upwind) and $\gamma = 1.75$ (filtered)
- Measuring convergence of the schemes with respect to grid refinement ($\Delta x$)
- Comparing time evolution at a fixed location $x = 0.5$
- Examining solution accuracy at a fixed time $t = 0.4$
- Testing both schemes on a **periodic initial condition** over long simulation times

---

## Implementation Details

- The filtered scheme is used with:

$$
\Delta t = 0.8 \cdot \Delta x \cdot \left( \frac{2 - \gamma}{2 + \gamma} \right) \quad \text{if } \gamma \neq 0, \quad \text{else } \Delta t = 0.8 \cdot \Delta x
$$

- The numerical update rule follows:

$$
\begin{aligned}
P_j^{n+1} = &\left( \gamma + (1 - \nu)\left(1 - \frac{\gamma}{2}\right) \right) P_j^n \\
&- \frac{\gamma}{2} P_j^{n-1} + \nu \left(1 - \frac{\gamma}{2} \right) P_{j-1}^n
\end{aligned}
$$

- Periodic simulations use:
  - $P[0, :] = \sin(2\pi x)$
  - Boundary values wrapped via `np.roll` for periodicity

---

## Key Components

- **Schemes analyzed**: basic upwind ($\gamma = 0$) and filtered ($\gamma = 1.75$)
- **Error vs $\Delta x$** at $t = 0.4$ computed for:
  - $\Delta x = 2^{-4}, 2^{-5}, \dots, 2^{-8}$
- **Evaluation points**:
  - Fixed spatial point $x = 0.5$
  - Fixed temporal point $t = 0.4$
- **Periodic test**:
  - Initial condition $\rho(x,0) = \sin(2\pi x)$
  - Evaluated at $t = 4, 10, 20$

---

## Results and Analysis

### Error Convergence

- Both $\gamma = 0$ and $\gamma = 1.75$ demonstrate consistent convergence as $\Delta x \to 0$
- Log-log error plots confirm **first-order accuracy**
- The filtered scheme consistently achieves lower absolute error at all tested $\Delta x$ values

### Temporal Profile at $x = 0.5$

- At $x = 0.5$, $\gamma = 1.75$ shows a **smoother transition** to the correct density compared to the upwind scheme
- Upwind exhibits a slightly earlier but more diffused transition

### Spatial Profile at $t = 0.4$

- The filtered scheme better aligns with the exact front at $x = vt$
- Upwind diffuses the discontinuity more, while the filtered scheme maintains sharper fronts

### Periodic Case

- Over long times, $\gamma = 1.75$ **preserves wave structure better**
- $\gamma = 0$ introduces more amplitude decay and phase lag by $t = 10T$
- The filtered scheme shows improved fidelity over repeated periodic advection

---

## Conclusion and What We Learned from Phases 1–3

### Phase 1:
- Introduced the **basic upwind scheme**
- Validated against exact solutions
- Measured errors and established baseline accuracy and convergence

### Phase 2:
- Introduced the **filtered scheme** parameterized by $\gamma$
- Observed improvements in **sharpness and smoothness**
- Began exploring how $\gamma$ affects stability and accuracy

### Phase 3:
- Directly compared **$\gamma = 0$ vs $\gamma = 1.75$**
- Demonstrated consistent **error reduction** and **wavefront accuracy** under filtering
- Verified that the filtered scheme better maintains structure in **periodic simulations** over long times

### Overall Takeaways:
- The filtered scheme retains the upwind method’s stability while improving accuracy
- $\gamma$ is a powerful tuning parameter for controlling diffusion and sharpness
- Periodic problems benefit from filtering, especially over long time integration
- Proper $\Delta t$ scaling with $\gamma$ is critical for maintaining CFL stability

---

[Return to Home →]({{ '/' | relative_url }}) 
