Given the following discretized equation for computing the density of cars using the traffic flow model:

$$
\begin{align}
P_{j}^{n+1} = (1-v)P_{j}^{n}+vP_{j-1}^{n}
\end{align}
$$

Where $v = \frac{\Delta t}{\Delta x}$, choose $\Delta x = \Delta t=.2$, and calculate the approximated density over the grid points for $0\leq x<1, 0\leq t\leq 1$ with the initial condition set to 0 and the boundary condition set to 0.5, i.e. $P_{j}^{0}, j =1,\dots,5, P_{0}^{n}=0.5, n =0,\dots,5$.
___
Solution:

| t/x | 0.0 | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |
| --- | --- | --- | --- | --- | --- | --- |
| 0.0 | 0.5 | 0   | 0   | 0   | 0   | 0   |
| 0.2 | 0.5 | 0.5 | 0   | 0   | 0   | 0   |
| 0.4 | 0.5 | 0.5 | 0.5 | 0   | 0   | 0   |
| 0.6 | 0.5 | 0.5 | 0.5 | 0.5 | 0   | 0   |
| 0.8 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0   |
| 1.0 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
