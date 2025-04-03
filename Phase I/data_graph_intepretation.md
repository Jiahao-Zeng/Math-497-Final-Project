For the Error vs Δx for different t values graph, we can see various t values plotted along a graph with an x-axis of Δx and a y-axis of the error. For each t value, the futher it gets from the starting point, the more the error increases. Reducing Δx reduces the error. As t increases, the error increases as well.
![Error vs Δx for different t value](approx_sol_surface.png)

For the Exact vs Approximated Solution at t=0.5, the exact solution has a sharp discontinuity at $x \approx 0.25$, indicating numerical diffusion, a common issue with methods like our upwind scheme we are using. The first-order upwind scheme introduces numerical diffusion (also called artificial viscosity), which smooths out sharp discontinuities in the solution.
![Exact vs Approximated Solution at t=0.5](error_vs_deltax.png)

For the Approximated Solution Surface, it is a solution curve that is consistent with our class findings. The area denoted by the color purple and yellow are flat, indicating a consistent density. In between the two flat points, there is a curve showing transition. If we decrease the step size, the numerical solution should better capture the steepness of the transition.
![Approximated Solution Surface](exact_vs_approx_t05.png)

Relating to the two exact vs approximate solution graphs, these show the discretization of approximating the density along x and t. The numerical solution only computes values at specific discrete points along x, rather than a continuous function. This is why the approximate solution may appear stepped or smoothed out compared to the exact solution. The grid resolution (Δx) determines how well sharp features can be fixed. A coarse grid introduces numerical diffusion, making transitions more gradual.
