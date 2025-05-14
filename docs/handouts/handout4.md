---
layout: handout
title: "Handout 4: Implementation Guide"
---

Given the following discretized equation for computing the density:

$$
P_{j}^{n+1} = (1 - \nu)P_{j}^{n} + \nu P_{j-1}^{n}
$$

Where $\nu = \frac{\Delta t}{\Delta x}$, and approximating density calculations over the grid points for $0 \leq x \leq 1$, $0 \leq t \leq 1$ with the initial condition set to 0 and the boundary condition set to 0.5, i.e. $P_{j}^{0}, j =1,\dots,M, P_{0}^{n}=0.5, n =0,\dots,N$, and the exact solution as 

$$
\rho(x,t) =
\begin{cases}
.5, & 0 \leq x < t \\
0, & t < x \leq 1
\end{cases}
$$

1. Calculate the approximate errors $\lvert \lvert E^{n} \rvert \rvert = \Delta x \sum_{j=0}^{M} \lvert P_{j}^{n} - P_{j}^{n} \rvert$ for $\Delta x = 0.1$; $\Delta t = \Delta x$ at $t=.2,.4,.6,.8,1$.

Consider the following two steps for a modified version of the upwind scheme:

$$
\begin{align}
\text{Step 1:} \qquad \qquad \qquad \quad \tilde{P}\_{j}^{n+1} = (1 - v)P\_{j}^{n} + vP\_{j-1}^{n} \\ 
\text{Step 2:} \quad P\_{j}^{n+1} = \tilde{P}\_{j}^{n+1} - \frac{\gamma}{2}(\tilde{P}\_{j}^{n+1} - 2P_{j}^{n} + P_{j}^{n-1})
\end{align}
$$


2. Combine the two step and algebraically show the following is obtained through the process:

$$
P_{j}^{n+1} = \left[ \gamma + (1 - v)\left( 1 - \frac{\gamma}{2} \right) \right] P_{j}^{n} - \frac{\gamma}{2}P_{j}^{n-1} + v\left( 1 - \frac{\gamma}{2} \right)P_{j-1}^{n}
$$

The above numerical scheme is known as the filtered upwind. Hint: eliminate $\tilde{P}_{j}^{n+1}$ from both steps.
