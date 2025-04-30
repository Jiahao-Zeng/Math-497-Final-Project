Three-point difference is a method for approximating the first derivative of a function at a point besides the Forward, Backward and Centered difference. Given the $h$ value $(h = x_{i+1}-x_{i})$, the three-point difference formula is as follows:
$$
\begin{align}
f'(x) \approx \frac{-3f(x)+4f(x_{i}+1)-f(x_{i+2})}{2h}
\end{align}
$$
Or
$$
\begin{align}
f'(x_{i}) \approx \frac{3f(x_{i})-4f(x_{i-1})+f(x_{i-2})}{2h}
\end{align}
$$
Note that the above two formulas show that the method could be applied as forward three-points or backward three-points difference formulas; i.e. using the next two consecutive points (forward) or the previous two consecutive points (backward).

1. Show that the error using this difference formula for approximating the first derivative at $x_{i}$ is $O(h^2)$. i.e.
$$
\begin{align}
\mid f'(x) \approx \frac{-3f(x)+4f(x_{i+1})-f(x_{i+2})}{2h} - f'(x_{i}) \leq O(h^2)\mid
\end{align}
$$
2. Let $f(x)=e^{2x+1}$. Approximate $f'(0)$ using both formulas with $h = 0.1, 0.01, 0.001$. Evaluate the approximation errors for all the above h values and show it is of order $h^2$

Solution for #1:
 - We must use Taylor series expansion
 Expansion for $f(x_{i+1})$ 
 $$
\begin{align}
&f(x+h) = f(x)+hf'(x)+\frac{h^{2}}{2!}f''(x)+\frac{h^{3}}{3!}f'''(x) \\
&f(x+2h)=f(x)+2hf'(x)+\frac{4h^{2}}{2}f''(x)+\frac{8h^{3}}{3!}f'''(x) \\
&\frac{-3f(x)+4\left[ f(x)+hf'(x)+\frac{h^{2}}{2!}f''(x)+\frac{h^{3}}{3!}f'''(x) \right]-\left[ f(x+2h)=f(x)+2hf'(x)+\frac{4h^{2}}{2}f''(x)+\frac{8h^{3}}{3!}f'''(x) \right]}{2h} \\
&\frac{2hf'(x)-\frac{4h^{3}}{6}f'''(x)}{2h} \\
&f'(x)-\frac{1}{3}h^{2}f'''(x)\leq O(h^{2})
\end{align}
$$

Solution for #2
The exact derivative of $f(x) = e^{2x+1}$:

$$
f'(x) = 2e^{2x+1}
f'(0) = 2e \approx 5.43656
$$
Using the three-point forward and backward difference formulas:
$$
\begin{align}
f'(0) \approx \frac{-3f(0) + 4f(h) - f(2h)}{2h} \\
f'(0) \approx \frac{3f(0) - 4f(-h) + f(-2h)}{2h} \\

\end{align}
$$

We compute the approximations and errors for different values of $h$:
$$
\begin{array}{|c|c|c|c|c|}
\hline
h & \text{Forward Approx.} & \text{Forward Error} & \text{Backward Approx.} & \text{Backward Error} \\
\hline
0.1 & 5.3521 & 0.0845 & 5.3740 & 0.0626 \\
0.01 & 5.4358 & 0.00074 & 5.4358 & 0.00071 \\
0.001 & 5.4366 & 0.0000073 & 5.4366 & 0.0000072 \\
\hline
\end{array}
$$
Observing the errors, we confirm that they decrease proportionally to $O(h^{2})$ validating the accuracy of the three-point difference formulas.