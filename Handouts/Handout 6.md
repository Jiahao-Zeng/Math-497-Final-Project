Given the traffic flow model:

$$
\rho_t + v \rho_x = 0
$$

$$
\rho(x,0) = \rho_0
$$

$$
\rho(0,t) = \rho_l
$$

Where $v \neq 1$ is the traffic flow speed limit and $0 \leq x \leq L$, $0 \leq t \leq T$. Consider the following discretization for car density $\rho$:

$$
\frac{p_j^{n+1} - p_j^n}{\Delta t} + v \frac{p_j^n - p_{j-1}^n}{\Delta x} = 0
$$

Where $p_j^n \approx \rho(x_j, t_n)$ for $j = 0,1, ..., M$; $n = 0,1, ..., N$.

1. Solve the above discretization for $p_j^{n+1}$.
2. How changing the velocity $v$ to a number different than 1 will change the formulation for the filtered upwind discretization.

$$
p_j^{n+1} = \left[ \gamma + (1-v) \left( 1 - \frac{\gamma}{2} \right) \right] p_j^n - \frac{\gamma}{2} p_{j+1}^n + v \left( 1 - \frac{\gamma}{2} \right) p_{j-1}^n
$$