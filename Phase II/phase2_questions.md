Given the following discretized equation for computing the density:

$$
P_j^{n+1} = \left[\gamma + (1 - \nu) \left(1 - \frac{\gamma}{2} \right) \right] P_j^n - \frac{\gamma}{2} P_j^{n-1} + \nu \left(1 - \frac{\gamma}{2} \right) P_{j-1}^n
$$


Where $\nu = \bar{v} \frac{\Delta t}{\Delta x}$, and approximating density calculations over the grid points for $0 \leq x \leq 1$, $0 \leq t \leq T$ with the initial condition set to 0 and the boundary condition set to $\rho_{l}$, i.e. $P_{j}^{0}=0$, $j=1,\dots,M,P_{0}^n=\rho_{l},n=0,\dots,N$, and the exact solution as 

$$
\rho(x, t) = \begin{cases} 
\rho_l, & 0 \leq x < \bar{v}t \\
0, & \bar{v}t < x \leq 1 
\end{cases}
$$

Start working on the following problems with $\rho_{l}=0.5$ and $\gamma=1.75$

1. Calculate the approximation errors $\|\|E^n\|\| = \Delta x \sum_{j=0}^M |\rho_j^n - P_j^n|$ for $\Delta x = \left( \frac{1}{2} \right)^i$, $i = 4, 5, 6, 7, 8$; See below for choice of $\Delta t$, at $t = .2, .4, .6, .8, 1$. Form a table of error values and plot the error values at $t = .4,\ 1$ vs different $\Delta x$ values.

2. Plot the exact solution and approximated solution for $0 \leq t \leq T$ at $x = .5$ with $\Delta x = \left( \frac{1}{2} \right)^6$; See below for choice of $\Delta t$.

3. Plot the exact solution and approximated solution for $0 \leq x \leq 1$ at $t = .5$ with $\Delta x = \left( \frac{1}{2} \right)^6$; See below for choice of $\Delta t$.

4. Plot the exact solution and approximated solution surfaces for $\Delta x = \left( \frac{1}{2} \right)^6$; See below for choice of $\Delta t$.

5. Interpret your data and graphs in parts 1 to 3 in terms of accuracy of the approximated solution and the contributing factors.

6. Repeat questions 1 to 5 for $\rho_L = 0.25,\ 0.75$.
