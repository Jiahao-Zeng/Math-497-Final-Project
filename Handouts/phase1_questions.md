# Final Project
## Phase 1

Given the following discretized equation for computing the density:

$$
P_j^{n+1} = (1 - \nu) P_j^n + \nu P_{j-1}^n
$$

Where $\nu = \frac{\Delta t}{\Delta x}$, and approximating density calculations over the grid points for $0 \le x \le 1$, $0 \le t \le T$ with the initial condition set to 0 and the boundary condition set to $\rho_l$, i.e. $P_j^0 = 0,j = 1,\dots,M$, $P_0^n = 0.5, n = 0,\dots,N$, and the exact solution as

$$
\rho(x,t) =
\begin{cases}
\rho_l, & 0 \le x < \nu t, \\
0, & \nu t < x \le 1.
\end{cases}
$$

Start working on the following problems with $\rho_l = 0.5$:

1. Calculate the approximation errors
   $$
   \|E^n\| = \Delta x \sum_{j=0}^M \lvert \rho_j^n - P_j^n\rvert
   $$
   for $\Delta x = (\tfrac12)^i$, $i = 3,4,5,6,7,8$; $\Delta t = 0.8\Delta x$ at $t = 0.2,0.4,0.6,0.8,1$. Form a table of error values and plot the error values at $t = 0.4,1$ vs. different $\Delta x$ values.

2. Plot the exact solution and approximated solution for $0 \le t \le 1$ at $x = 0.5$ with $\Delta x = (\tfrac12)^6$; $\Delta t = 0.8\Delta x$.

3. Plot the exact solution and approximated solution for $0 \le x \le 1$ at $t = 0.5$ with $\Delta x = (\tfrac12)^6$; $\Delta t = 0.8\Delta x$.

4. Plot the exact solution and approximated solution surfaces for $\Delta x = (\tfrac12)^6$; $\Delta t = 0.8\Delta x$.

5. Interpret your data and graphs in parts 1 to 3 in terms of accuracy of the approximated solution and the contributing factors.

6. Repeat questions 1 to 5 by changing the boundary condition $\rho_l$ to 0.75.
