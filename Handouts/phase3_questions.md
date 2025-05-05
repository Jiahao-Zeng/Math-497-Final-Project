# Final Project
## Phase 3

Given the following discretized equation for computing the density:

$$
P_j^{n+1} = \left[\gamma + (1 - \nu) \left(1 - \frac{\gamma}{2} \right) \right] P_j^n - \frac{\gamma}{2} P_j^{n-1} + \nu \left(1 - \frac{\gamma}{2} \right) P_{j-1}^{n}
$$


Where $\nu = \bar{v} \frac{\Delta t}{\Delta x}$, and approximating density calculations over the grid points for $0 \leq x \leq 1$, $0 \leq t \leq T$ with the initial condition set to 0 and the boundary condition set to $\rho_{l}$, i.e. $P_{j}^{0}=0$, $j=1,\dots,M,P_{0}^n=\rho_{l},n=0,\dots,N$, and the exact solution as 

$$
\rho(x, t) = \begin{cases} 
\rho_l, & 0 \leq x < \bar{v}t \\
0, & \bar{v}t < x \leq 1 
\end{cases}
$$

Start working on the following problems with $\rho_{l}=0.5$ and $\gamma=1.75$

1. Calculate the approximation errors $\text{||} E^n \text{||} = \Delta x \sum_{j=0}^M |\rho_j^n - P_j^n|$ for $\Delta x = \left( \frac{1}{2} \right)^i$, $i = 4, 5, 6, 7, 8$; See below for choice of $\Delta t$ and use the $\gamma = 1.75$ for the size of time step, at $t = .2, .4$. Plot the error values at $t = .4$ vs different $\Delta x$ values and for both $\gamma = 0, 1.75$.

2. Plot the exact solution and approximated solutions with $\gamma = 0, 1.75$ for $0 \leq t \leq T$ at $x = .5$ with $\Delta x = \left( \frac{1}{2} \right)^6$; See below for choice of $\Delta t$ using $\gamma = 1.75$.

3. Plot the exact solution and approximated solution for $0 \leq x leq 1$ at $t = .4$ with $\Delta x = \left( \frac{1}{2} \right)^{6}$; See below for choice of $\Delta t$ using $\gamma = 1.75$

4. Interpret your data and graphs in part 1 to 3 in terms of accuracy of the approximated solutions and the contributing factors.

5. Adjust your initial and boundary conditions as following:

$$
\begin{gather} \\
\rho(x, 0) = \rho_{0}(x) = \sin(2\pi x) \\
\rho(0, t) = \rho(1, t)
\end{gather}
$$

Use the aboved discretized equation for computing the density for $0 \leq x \leq 1$, $0 \leq t \leq 10T$ with $\gamma = 0, 1.75$, $\Delta x = \left( \frac{1}{2} \right)^{8}$, See below for choice of $\Delta t$ using $\gamma = 1.75$. The exact solution ffor this problem is $\rho(x, t) = \sin(2\pi x)$. 
Plot the exact soltuion with the approximate solutions together in one screen at different times; $t = 2T, 5T, 10T$.

Bonus: Make a movie of how the exact solution along with both approximated solutions move through time.

The velocity and final time values for your projects are selected as follows:

1. $\bar{v} = 0.5$, $T = 2$, $\Delta t = 0.8 \Delta x \left( \frac{2 - \gamma}{2 + \gamma} \right)$; Team 4 
2. $\bar{v} = 0.75$, $T = 2$, $\Delta t = 0.8 \Delta x \left( \frac{2 - \gamma}{2 + \gamma} \right)$; Team 2
3. $\bar{v} = 1.25$, $T = \frac{5}{4}$, $\Delta t = 0.8 \Delta x \frac{1}{\bar{v}} \left( \frac{2 - \gamma}{2 + \gamma} \right)$; Team 3
4. $\bar{v} = 1.5$, $T = \frac{3}{2}$, $\Delta t = 0.8 \Delta x \frac{1}{\bar{v}} \left( \frac{2 - \gamma}{2 + \gamma} \right)$; Team 5
5. $\bar{v} = 1.75$, $T = \frac{7}{4}$, $\Delta t = 0.8 \Delta x \frac{1}{\bar{v}} \left( \frac{2 - \gamma}{2 + \gamma} \right)$; Team 1
